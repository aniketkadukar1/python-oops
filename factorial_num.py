"""Find the factorial of given number using recusion"""

num = int(input("Enter the num: "))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(num))