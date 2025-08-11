class Car:
    def drive(self):
        print ("Car is driving")

class Toyota(Car):
    def speed(self):
        print ("Toyota is speeding")

class Honda(Car):
    def drift(self):
        print ("Honda is drifting")              

t = Toyota()
h = Honda()

t.drive()
t.speed()
h.drive()
h.drift()