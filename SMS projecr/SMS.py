class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name} Age: {self.age} years old.")
class student(person):
    school="ABC School"
    def __init__(self,name,age,roll,class_name,marks):
        super().__init__(name,age)
        self.roll = roll
        self.class_name=class_name
        self.marks = marks
    def show_info(self):
        super().show_info()
        print(f"school: {self.school} class: {self.class_name} roll:{self.roll}")
    def get_marks(self):
        if 0<= marks <=100:
            self._marks = marks
        else:
            print("please enter valid marks between 0 and 100")
    def __del__(self):
        print(f"student : {self.name} is deleted.")

class teacher(person):
    def __init__(self, name, age, emp_id, subject, position):
        super().__init__(name,age,emp_id,subject)
        self.position = position
    def show_info(self):
        super().show_info()
    def add_student(self,student_list,student):
        student_list.append(student)
        print(f"student {}")

    
