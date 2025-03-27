"""
name = "Lydia"
# Swap exercise 

a = 5 
b = 10 
a,b = b,a
print(a,b)
# calculate the area of a rectangle
length = int(input("Enter the length of the rectangle: "))
width =  int(input("Enter the width of the rectangle:"))
Area = length * width
print(Area)
celcius = int(input("Enter temprature in degree celcius:"))
Fahrenheit = (9/5 * celcius )+ 32
print(Fahrenheit)
# Simple interest exercise 
p = int(input("Enter the pricipal amount:"))
r = int(input("Enter the rate of interest:"))
t = int(input("Enter time in years:"))
simple_interest = p*r*t/100
print(simple_interest)
name = "Python"
print(type(name))
# get user input 
name  = input("Enter your name:")
age = int(input("Enter your age:"))
print(f"My name is , {name} and I am {age} years old:")

# Conditional exercise 
num = int (input("Enter a number:"))
if num % 2 == 0 :
    print("num is even")
else:
    print("num is odd")

num_one = int (input("Enter a number:"))
if num_one > 0 :
    print("num is positive")
elif num_one == 0:
    print("num is zero")
else:
    print("num is negative")

a = int (input("Enter  the first integer number:"))
b = int (input("Enter the second integer  number:"))
c = int(input("Enter the third integer number:"))
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")
# Grade calculator 
score = int(input("Enter your score:"))
if score <= 100 and score >= 90:
    print("Your score is A.")
elif score <= 89 and score >= 80:
    print("Your score is B.")
elif score <= 79 and score >= 70:
    print("Your score is C.") 
elif score <= 69 and score >= 60:
    print("Your score is D.")
else:
    print("Your score is F.12") 
    """
# rock paper scissor game 
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Choose rock, paper, or scissors: ").lower()

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win! Computer chose", computer)
else:
    print("You lose! Computer chose", computer)

