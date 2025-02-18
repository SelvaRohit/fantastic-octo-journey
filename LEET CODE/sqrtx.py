# x=16
# start = 1
# end=46340
# flag=0
# mid_list=[]
# previous=0
# while(end>=start):
#     mid=((end-start)//2)+start
#     # print(mid)
#     if(mid*mid == x):
#         mid_list.append(mid)
#         break
#     elif(mid*mid>x):
#         flag=-1
#         if(previous==1):
#             print("123")
#             mid_list.append(mid)
#             break
#         else:
#             mid_list.append(mid)
#             previous=flag
#         end=mid-1
#     else:
#         flag=1
#         if(previous==-1):
#             print("456")
#             mid_list.append(mid)
#             break
#         else:
#             mid_list.append(mid)
#             previous=flag
#         start=mid+1
# print(mid)
# print(start)
# print(end)
# print(mid_list)
    

x=0
start = 1
end=46340
flag=0
# mid_list=[]
previous=0
while(end>=start):
    mid=((end-start)//2)+start
    # print(mid)
    if(mid*mid == x):
        previous=0
        # mid_list.append(mid)
        end = mid
        break
    elif(mid*mid>x):
        flag=-1
        # mid_list.append(mid)
        previous=flag
        end=mid-1
    else:
        flag=1
        # mid_list.append(mid)
        previous=flag
        start=mid+1
print(end)

    

