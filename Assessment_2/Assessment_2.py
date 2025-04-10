import csv

# Base Class: Person
class Person:
    def __init__(self, person_id):
        self._person_id = person_id

    def get_summary(self):
        return f"Person ID: {self._person_id}"

# Sub Class: Student
class Student(Person):
    def __init__(self, person_id, credits_completed, gpa):
        super().__init__(person_id)
        self._credits_completed = credits_completed
        self._gpa = gpa

    def graduation_readiness(self):
        if self._credits_completed >= 120 and self._gpa >= 2.0:
            return "Ready for graduation"
        else:
            return "Not ready for graduation"

    def get_summary(self):
        return (f"Student ID: {self._person_id}, Level: Undergraduate, GPA: {self._gpa}, "
                f"Credits Completed: {self._credits_completed}, Graduation Status: {self.graduation_readiness()}")

# Sub Class: MasterStudent
class MasterStudent(Person):
    def __init__(self, person_id, thesis_title, publications, study_duration):
        super().__init__(person_id)
        self._thesis_title = thesis_title
        self._publications = publications
        self._study_duration = study_duration

    def graduation_readiness(self):
        if self._publications >= 1 and self._study_duration >= 2:
            return "Ready for graduation"
        else:
            return "Not ready for graduation"

    def get_summary(self):
        return (f"Student ID: {self._person_id}, Level: Master\n"
                f"Thesis Title: {self._thesis_title}\n"
                f"Publications: {self._publications}\n"
                f"Years of Study: {self._study_duration}\n"
                f"Graduation Status: {self.graduation_readiness()}")

# Load data from CSV file
def load_data(file_name):
    students = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header
        for row in reader:
            person_id, level, credits_completed, gpa, thesis_title, publications, study_duration = row
            credits_completed = int(credits_completed)
            gpa = float(gpa)
            publications = int(publications)
            study_duration = float(study_duration)
            
            if level == 'Undergraduate':
                students.append(Student(person_id, credits_completed, gpa))
            elif level == 'Master':
                students.append(MasterStudent(person_id, thesis_title, publications, study_duration))
    return students

# Get students ready for graduation
def get_students_ready_for_graduation(students):
    print("Students Ready for Graduation:")
    for student in students:
        if student.graduation_readiness() == "Ready for graduation":
            print(f"- {student._person_id}: Ready for graduation.")

# Show probation list
def show_probation_list(students):
    print("Probation List (GPA < 2.0):")
    for student in students:
        if isinstance(student, Student) and student._gpa < 2.0:
            print(f"- {student._person_id}: GPA {student._gpa:.2f}")

# Retrieve student details by ID
def get_student_by_id(students, student_id):
    for student in students:
        if student._person_id == student_id:
            print(student.get_summary())
            return
    print(f"Invalid student ID: {student_id}")


# Main
uni_students = load_data("oop_uni_students.csv")
get_students_ready_for_graduation(uni_students)
show_probation_list(uni_students)

get_student_by_id(uni_students, 'S0001')  
get_student_by_id(uni_students, 'S11')    # Invalid 
get_student_by_id(uni_students, 'M0002')  