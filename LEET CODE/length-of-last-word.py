# s="   fly me   to   the moon  "
s="Hello World"
iteration=len(s)-1
flag=1
start,end=0,0
while(flag>=0 and iteration>-1):
    # print(iteration)
    # print(flag)
    # print(s[iteration])
    # if(flag==1 and s[iteration]==" "):
    #     # iteration-=1
    #     pass
    # # elif(s[iteration]!=" " and flag==0):
    # #     pass
    if(s[iteration]!=" " and flag==1):
        flag=0
        # iteration-=1
        end=iteration-1
    elif(flag==0 and s[iteration]==" "):
        start=iteration+1
        flag = -1
    iteration-=1
print(start,end)
print(s[start:end+2])
print(len(s[start:end+2]))

