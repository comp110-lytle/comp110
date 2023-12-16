class Course:
    name: str
    level: int
    prerequisites: list[str]
    
    def is_valid_course(self, prereq_name: str) -> bool:
        if self.level >= 400:
            for req in self.prerequisites:
                if req == prereq_name:
                    return True
        return False
    
    

def find_courses(clist: list[Course], req_name: str) -> list[str]:
    prereq_list : list[str] = []
    for course in clist:
        if course.level >= 400:
            for elem in course.prerequisites:
                if elem == req_name:
                    prereq_list.append(course.name)
    return prereq_list


