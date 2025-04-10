# Base Class: Person 
class Person: 
    def __init__(self, person_id, name, age): 
        self.person_id = person_id 
        self.name = name 
        self.age = int(age) 
        
    def display_info(self): 
        print(f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}") 
        
# Subclass: Student 
class Student(Person): 
    def __init__(self, student_id, name, age, major, cgpa): 
        super().__init__(student_id, name, age) 
        self.major = major 
        self.cgpa = float(cgpa) if cgpa else 0.0 # Convert to float 
        
    def display_info(self): 
        print(f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Role: Student, " 
              f"Major: {self.major}, CGPA: {self.cgpa:.2f}") 
        
# Subclass: Staff 
class Staff(Person): 
    def __init__(self, staff_id, name, age, major, years_experience): 
        super().__init__(staff_id, name, age) 
        self.major = major 
        self.years_experience = int(years_experience) if years_experience else 0 # Convert to int 
        
    def display_info(self): 
        print(f"ID: {self.person_id}, Name: {self.name}, Age: {self.age}, Role: Staff, " 
              f"Major: {self.major}, Experience: {self.years_experience} years") 
        
# Function to load data from CSV file 
def load_data(filename):
    people = [] 
    try: 
        with open(filename, mode='r', encoding='utf-8') as file: 
            lines = file.readlines() 
            headers = lines[0].strip().split(",") # Extract headers 
            for line in lines[1:]: 
                data = line.strip().split(",") # Read each row 
                person_data = dict(zip(headers, data)) # Map headers 

                major = person_data["Major"] 
                cgpa = person_data["CGPA"] 
                years_experience = person_data["YearsExperience"]
                if cgpa: 
                    person = Student(person_data["ID"], person_data["Name"], person_data["Age"], major, cgpa) 

                elif years_experience: 
                    person = Staff(person_data["ID"], person_data["Name"], person_data["Age"], major, years_experience) 
                
                else: 
                    person = Person(person_data["ID"], person_data["Name"], person_data["Age"]) 
                
                people.append(person) 
            
        print("Data successfully loaded from", filename) 
    except FileNotFoundError: 
        print(f"File '{filename}' not found.") 
    return people 

# Function to display all people 
def display_people(people): 
    print("\nPeople List:") 
    for person in people: 
        person.display_info() # Function to get students with CGPA < 2.0 
        
def get_students_below_2_cgpa(people): 
    print("\nStudents with CGPA < 2.0:") 
    for person in people: 
        if isinstance(person, Student) and person.cgpa < 2.0: 
            person.display_info() # Function to get staff with ≥10 years experience 

def get_staff_with_10_plus_years(people): 
    print("\nStaff with >= 10 years of experience:") 
    for person in people: 
        if isinstance(person, Staff) and person.years_experience >= 10: 
            person.display_info() 

# Main Execution 
people = load_data("persons.csv") 
display_people(people) 
get_students_below_2_cgpa(people) 
get_staff_with_10_plus_years(people)