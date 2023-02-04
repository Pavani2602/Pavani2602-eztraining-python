#project-3-flame+s+


name1=input("enter the name1: ").lower()
name2=input("enter the name2: ").lower()
#if you give first and last name
#with space in between
name1=name1.replace(" "," ")
name2=name2.replace(" "," ")
print(name1)
print(name2)
for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
count=len(name1+name2)
print(count)
if count>0:
    list1=["Friends","Lovers","Attarction","Marriage","Enemies","Sisters"]
    while len(list1)>1:
        c=count%len(list1)
        s_index=c-1
        if s_index>=0:
            left=list1[:s_index]
            right=list1[s_index+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("Relationship :",list1[0])
else:
    print("Enter differengt names")
            
