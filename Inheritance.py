class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog is inheriting from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # This comes from Animal!
d.bark()   # This comes from Dog
