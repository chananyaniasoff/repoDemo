import random
import os

def cls(): return os.system('cls')

cls()


print("print to our first github project")
name=input("what is your name?")
print(f"welcome to you {name}")

print(f"{name.title()} your name has {len(name)}")

for letter in name:
    print(letter)

for index, letter in enumerate(name):
    print(f"{index+1}:{letter}")
    if letter=="c":
        print("my name!!")
    else:
        print("😊")   
         



