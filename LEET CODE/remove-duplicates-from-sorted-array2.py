nums = [0,0,1,1,1,2,2,3,3,4,4,4,4]
len_nums=len(nums)
i=0
while(i<len_nums):
    print(i)
    if(nums[i] == '_'):
        break
    elif(nums[i] in nums[i+1 : len_nums]):
        nums.remove(nums[i])
        nums.append('_')
        i-=1
    i+=1
    print(nums)
    print(i)
#         print(i)
#         print(element)
#         print(nums)
# print(nums)
