l1=[1]
l2=[0]
i=j=0
temp=[]
while l1 and l2:
    if l1[0]<l2[0]:
        temp.append(l1.pop(0))

    else:
        temp.append(l2.pop(0))
temp=temp+l1 if l1 else temp+l2
print(temp)