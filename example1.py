# Basic Encapsulation with private varibable

class student:
    def __init__ (self, name, marks):
        self.__name = name         # private attribute
        self.__marks = marks       # private attribute

# getter method
    def get_marks(self):
        return self.__marks 

# setter method
    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Marks canot be negative!")

s1 = student("Swajit", 90) 

print(s1.get_marks())          # accessing through getter

 