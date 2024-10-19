""" Below is the example of polymorphism..."""

class English:
    def greet(self):
        print("hello...")

class French:
    def greet(self):
        print("banjour...")

def greetings(obj):
    obj.greet()

e = English()
f = French()
greetings(e)
greetings(f)