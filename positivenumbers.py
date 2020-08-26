#Input: list1 = [12, -7, 5, 64, -14]
#Input: list2 = [12, 14, -95, 3]
list1=[]
print("the list is : ",list1)
n=int(input("enter the number of elements are there in the list : "))

for i in range(n):
    list1.append(int(input("enter the element : ")))

print(list1)
finallist = []
for positivenumberlist in list1:
    if positivenumberlist<0:
        print("negative!")
    else :
        finallist.append(positivenumberlist)

print(finallist)
