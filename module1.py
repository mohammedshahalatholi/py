print("enter the x and y")



x=int(input("enter value 1"))
y=int(input("enter value 2"))

rec=x*y

print("area of rectangle",rec)

car={'Brand':"bmv","Model":"Q7",'Year':2024}

print(car["Model"])

for i in car:
    print(i,':',car[i])

bikemodel=["bullet","honda","ninja"]

print(bikemodel)

for n in bikemodel:
    print(n)

div=x%5
if div==0:
    print(div)
    print("x is divisible by 5")

else:
    print(div)
    print("not devisible by 5")
