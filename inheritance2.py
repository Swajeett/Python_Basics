class vehicle:
    def drive(self):
        print ("Vehicle is driving")

class bike(vehicle):
    def speed(self):
        print ("Bike is speeding")

b = bike()
b.drive()
b.speed()

        