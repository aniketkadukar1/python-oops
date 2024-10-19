class Robot:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Hi, my name is " + self.name)

class PoliceRobot(Robot):
    def say_hi(self):
        print("I want to become PiliceRobot")

pr = PoliceRobot("Raju")
pr.say_hi()