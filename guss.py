import numbers
import random


number1 = int(input("the range yo want to from  "))
number2= int(input("to  "))
n = random.randint(number1,number2)
print("****************",n)

guess=int(input("\nthe number is "))



while guess!=n:
    if guess>n:
        print("try again the number is more less")
        guess=int(input("\nthe number is "))
    if guess<n:
        print("try again the number is more higer")
        guess=int(input("\nthe number is "))

print("you win !!!!!")        