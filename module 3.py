#Create a Function for Addition Write a function that takes two numbers as input and returns their sum.

x=int(input("Enter the first value"))

y= int(input("enter the second value"))

def sum(x,y):
    add=x+y
    return add
print("function called")

print(sum(x,y))


#Factorial Using a Function Create a function to calculate the factorial of a number.

def fact(x):
    facto=1
    for i in range(1,x):
        facto=i*facto
        print(i,"x",facto,"=",facto)

    return 0

fact(x)