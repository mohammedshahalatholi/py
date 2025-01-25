for i in range(1,50):
    if i%2==0:
        print(i)


fruits=["mango","apple","grape"]

print(fruits[1])

for i in fruits:
    print(i.upper())


for i in range(10,0,-1):
    print(i)
print("first 10 multiple of three")
x=1
while (x<=15):
    print(x*3)
    x=x+1
    if (x>10):
        print("exicuting brake")
        break
x=0
count=0
while x<1:
    print("exicuting")
    cntrl=input("Type stop for the stop exicution")
    count+=1
    if cntrl=="stop":
        print("exicution stoped in iteration of", count)
        break

fact=int(input("enter the number for factorial"))

print("enterd number is ",fact)
x=1
tmp=1
while(x!=fact):
    tmp=x*tmp
    print(tmp)
    x=x+1

print("other method")
result=1
while fact>0:
    result *=fact
    fact-=1
    print(fact)
print("even number")
for i in range(2,10,2):
    print(i)