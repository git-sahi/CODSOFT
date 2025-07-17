import random as r
import string as s

def PassEasy(length): #password including only numbers
    characters = s.digits
    Easypwd = ''.join(r.choice(characters) for i in range(length))
    return Easypwd

def PassMed(length):  #password including letter and numbers
    characters = s.ascii_letters + s.digits
    Medpwd = ''.join(r.choice(characters) for i in range(length))
    return Medpwd

def PassHard(length):  #password including numbers, letter and symbols
    characters = s.ascii_letters + s.digits + s.punctuation
    Hardpwd =  ''.join(r.choice(characters) for i in range(length))
    return Hardpwd

def PasswordGenerator(length , complexity):
    if complexity == 'HIGH':
        return PassHard(length)

    elif complexity == 'MEDIUM':
        return PassMed(length)
    
    elif complexity == 'EASY':
        return PassEasy(length)
    
    else:
        print("invalid complexity")
        return None

#main
try:
    length = int(input("Please enter the length of the password you want:"))
    if length <= 0:
        raise ValueError("password length must be positive")
except ValueError as e:
    print("Invalid Password:" , e)
    exit()

    
print("Complexity:")
print("High")
print("Medium")
print("Easy")
complexity = input("Enter the complexity:").upper()


pwd = PasswordGenerator(length , complexity)
if pwd:
    print("Generated password:", pwd)
else:
    print("Invalid complexity level. Please choose High, Medium, or Easy.")