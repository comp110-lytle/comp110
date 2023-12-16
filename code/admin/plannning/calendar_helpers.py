"""Calendar Helpers"""

from MplCalendar import MplCalendar
import calendar
from helpers import Kind

class CourseCal(MplCalendar):
    
    """Extends MplCalendar"""
    
    def __init__(self, year, month, syllabus):
        MplCalendar.__init__(self,year,month)
        self.syllabus = syllabus
    
    def color_class_days(self, color: str):
        for current_date in self.syllabus:
            if self.month == current_date.month:
                for plan in self.syllabus[current_date]:
                    if plan.kind == Kind.CL:
                        self.color_day(current_date.day, color)

    def mark_holidays(self, holidays):
        for date in holidays:
            if self.month == date.month:
                self.add_event(date.day, 'Holiday')
                
    def mark_lessons(self):
        for current_date in self.syllabus:
            if self.month == current_date.month:
                for plan in self.syllabus[current_date]:
                    if plan.kind == Kind.CL and not ("Day" in plan.title):
                        self.add_event(current_date.day, plan.title, "purple")

    def mark_EX(self):
        outstanding: Dict[date, List[Plan]] = {}
        # Get release dates
        for current_date in self.syllabus:
            for plan in self.syllabus[current_date]:
                if (self.month == current_date.month) and (plan.kind == Kind.EX):
                        rep = f"{plan.kind.name}{plan.n:02} Out"
                        self.add_event(current_date.day, rep, "green")
                if (plan.kind == Kind.EX) and (plan.deadline is not None):
                    if plan.extension in outstanding:
                        outstanding[plan.extension].append(plan)
                    else:
                        outstanding[plan.extension] = [plan]
        for due_date in outstanding:
            if self.month == due_date.month:
                for elem in outstanding[due_date]:
                    title = f"{elem.kind.name}{elem.n:02} Due"
                    self.add_event(due_date.day, title, "red")
                    
