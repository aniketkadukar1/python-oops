text = str(input("Enter the string: "))

def check_palindrom(text):
    first = 0
    last = len(text) - 1

    while first < last:
        if text[first] == text[last]:
            first += 1
            last -= 1
        else:
            return False
    
    return True

print(check_palindrom(text))