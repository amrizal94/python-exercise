class Student:
    def __init__(self, name, scores):
        self.__name = name
        self.__courses = {}
        self.__scores = scores
        
    def add_course(self, course, score):
        """_summary_
        Args:
            If score is 90 or above the function should return "A"
            If score is between 80 and 89 the function should return "B"
            If score is between 70 and 79 the function should return "C"
            If score is between 60 and 69 the function should return "D"
            Otherwise, the function should return "F"
        """        
        if score >= 90:
            self.__courses[course] = "A"
        elif score >= 80:
            self.__courses[course] = "B"
        elif score >= 70:
            self.__courses[course] = "C"
        else:
            self.__courses[course] = "F"
    
    def get_courses(self):
        return self.__courses
    
# don't touch below this line


def test(student_name, courses, scores):
    student = Student(student_name, scores)
    print(f"Student created: {student_name}")

    for i, course in enumerate(courses):
        student.add_course(course, scores[i])
        print(f"Added course: {course} with score: {scores[i]}")
    courses = student.get_courses()
    for course in courses:
        print(f"{student_name}'s grade in {course} is a {courses[course]}")
    test_encapsulation(student)
    print("=====================================")


def test_encapsulation(student):
    try:
        print(student.__courses)
    except:
        print("Private data member is encapsulated properly")


def main():
    test("John Thorton", ["Math", "English", "History"], [85, 92, 76])
    test("Jasper Allen", ["Science", "Social Studies"], [90, 88])
    test(
        "Bobby Christensen",
        ["Physics", "Chemistry", "Biology", "Geology"],
        [80, 78, 85, 90],
    )


main()
