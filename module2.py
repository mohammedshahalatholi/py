# Write a program that checks whether a given number is even or odd

x=int(input("Enter the value"))
x=x%2
if x==0:
    print("its a even number")
else:
    print("Odd number")

#Create a program that prints the multiplication table for numbers 1 through 10.

for i in range(1,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)


#Given a list of numbers, use list comprehension to create a new list containing the squares of the even numbers only.


newlist=[N**2 for N in range(1,10) if N%2==0]
print("list")
print(newlist)