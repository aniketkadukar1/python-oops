
#Lambda Functions
multiply = lambda x, y : (x+1) * y
print(multiply(2, 4))


#Python decorators
def new_decorator(my_function):
    def wrapper():
        print("This message will display before the function")
        my_function()
        print("This message will desplay after method call")
    return wrapper

@new_decorator
def my_new_method():
    print("Hiii....")

my_new_method()
