"""Automating Gradescope via Selenium."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"


from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time
from datetime import datetime

class GradescopeDriver:

    driver: RemoteWebDriver
    logged_in: bool = False

    def __init__(self, email: str, password: str):
        self.driver = webdriver.Chrome()
        self.login(email, password)

    def login(self, email: str, password: str) -> None:
        self.driver.get("https://www.gradescope.com/login")
        email_elem = self.driver.find_element(By.ID, "session_email")
        email_elem.send_keys(email)
        password_elem = self.driver.find_element(By.ID, "session_password")
        password_elem.send_keys(password)
        password_elem.send_keys(Keys.RETURN)
        self.logged_in = "Your Courses" in self.driver.title
        assert self.logged_in

    def get_course(self, id: int) -> "GradescopeCourse":
        return GradescopeCourse(self, id)


class GradescopeCourse:

    gradescope: GradescopeDriver
    driver: RemoteWebDriver
    id: int
    number: str
    name: str

    def __init__(self, gradescope: GradescopeDriver, id: int):
        self.gradescope = gradescope
        self.driver = gradescope.driver
        self.id = id
        # Load Course Info
        self.gradescope.driver.get(f"https://gradescope.com/courses/{self.id}/edit")
        self.number = self.gradescope.driver.find_element(By.ID, "course_shortname").get_attribute("value")
        self.name = self.gradescope.driver.find_element(By.ID, "course_name").get_attribute("value")

    def __str__(self) -> str:
        return f"GradescopeCourse - {self.number}: {self.name}"

    def get_assignments(self) -> dict[str, "GradescopeAssignment"]:
        self.gradescope.driver.get(f"https://gradescope.com/courses/{self.id}/assignments")
        # Sort by Release Date ASC
        self.gradescope.driver.find_element(By.CSS_SELECTOR, "#assignments-instructor-table th:nth-child(3)").click()
        # Grab assignment elements
        assignment_elems = self.gradescope.driver.find_elements(By.CSS_SELECTOR, "#assignments-instructor-table tr td:first-child a")
        assignments: dict[str, "GradescopeAssignment"] = {}
        for assignment_elem in assignment_elems:
            href = assignment_elem.get_attribute("href")
            id = re.sub("^.*\/([0-9]+)$", '\\1', href)
            title = assignment_elem.text
            code = re.sub("(....).*", '\\1', title)
            if code[:2] != 'QZ':
                assert code not in assignments
            assignments[code] = GradescopeAssignment(self, title, id)
        return assignments



class GradescopeScraper:
    driver: RemoteWebDriver

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver

    def get_value(self, id: str) -> str:
        elem = self.driver.find_element(By.ID, id)
        return elem.get_attribute("value")

    def set_value(self, id: str, value: str) -> None:
        elem = self.driver.find_element(By.ID, id)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.TAB)

    def get_datetime_value(self, id: str) -> datetime | None:
        try:
            return datetime.strptime(self.get_value(id), "%m/%d/%Y, %I:%M %p")
        except:
            return None

    def set_datetime_value(self, id: str, value: datetime) -> None:
        print(datetime.strftime(value, "%m/%d/%Y, %I:%M %p"))
        datetime_as_str = datetime.strftime(value, "%m%d%Y%I%M%p") # Spaces removed due to Gradescope js
        self.set_value(id, datetime_as_str)

    def get_checked(self, id: str) -> bool:
        elem = self.driver.find_element(By.ID, id)
        return elem.is_selected()

    def set_checked(self, id: str, checked: bool) -> None:
        if checked != self.get_checked(id):
            elem = self.driver.find_element(By.ID, id)
            elem.send_keys(Keys.SPACE)

    def submit(self) -> None:
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'form.js-assignmentForm input[type="submit"]')
        submit_button.click()

class GradescopeAssignment(GradescopeScraper):

    course: GradescopeCourse
    title: str
    id: int
    loaded: bool = False

    release_date: datetime
    due_date: datetime
    allow_late_submissions: bool
    late_due_date: datetime

    def __init__(self, course: GradescopeCourse, title: str, id: str):
        super().__init__(course.driver)
        self.course = course 
        self.id = id
        self.title = title

    def __repr__(self) -> str:
        return f"GradescopeAssignment - {self.id}: {self.title}"

    def load(self) -> None:
        self.driver.get(f"https://www.gradescope.com/courses/{self.course.id}/assignments/{self.id}/edit")
        self.release_date = self.get_datetime_value("assignment_release_date_string")
        self.due_date = self.get_datetime_value("assignment_due_date_string")
        self.allow_late_submissions = self.get_checked("assignment_allow_late_submissions")
        self.late_due_date = self.get_datetime_value("assignment_hard_due_date_string")
        self.loaded = True

    def persist(self) -> None:
        self.driver.get(f"https://www.gradescope.com/courses/{self.course.id}/assignments/{self.id}/edit")
        self.set_datetime_value("assignment_release_date_string", self.release_date)
        self.set_datetime_value("assignment_due_date_string", self.due_date)
        self.set_checked("assignment_allow_late_submissions", self.allow_late_submissions)
        if self.allow_late_submissions:
            self.set_datetime_value("assignment_hard_due_date_string", self.late_due_date)

        if len(self.driver.find_elements(By.CLASS_NAME, "error-msg")) > 0:
            print(f"Error persisting '{self.title}': check due dates")
        else:
            self.submit()
