a=[]
#sortlist=[]
n=int(input("enter the n"))

for i in range(n):
    value=input("enter the value for list")
    no = int(input("enter the no"))
    a.append([value,no])


sortlist=sorted(set(no for _,no in a))
secontlowest=sortlist[1]
print("list")
print(a)
print("lowest = ",secontlowest)
secontloweststudentname=sorted([value for value,no in a if no==secontlowest ])
print("sorted",sortlist)

print("second lowest student name",secontloweststudentname)

for i in secontloweststudentname:
    print(a)