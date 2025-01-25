
b= int(input("Enter the num"))
def square(a):
    square=a*a
    print(square)

square(b)

def grater(a,b):
    if a>b:
        print("A is grater")
    elif a==0| b==0:
        print("A or B is zero")

    else:
        print("B is grater")

a=int(input("Enter the A"))

b=int(input("Enter b"))
grater(a,b)
list=[1,2,3,4,5,6]
lisvalue=int(input("add values to list"))

list.append(lisvalue)


print("perticulr number")
for i in list:
    print(i)
print("add of list")
def addlist(list):
    add=0
    for i in list:
        add=i+add
    return add

addoflist=addlist(list)
print(addoflist)


number=int(input("enter the number to check even or odd"))

def check(x):
    if x%2==0 & x!=0:
        print("Even")
    elif x==0:
        print("Its zero")
    else:
        print("odd")

check(number)
# Write a function to generate the factorial of a number using a loop.
xfact=int(input("Enter number for factorial"))
def factoriyal(xfact):
    count=1
    for i in range(1,xfact+1):
        i=i*count
        count=i

        print(count)


factoriyal(xfact)


