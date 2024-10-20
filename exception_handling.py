try:
    result = 10/0
    print(result)
except:
    print("Some error occured")
else:
    print("---")
finally:
    print("Exception is handled successfully")