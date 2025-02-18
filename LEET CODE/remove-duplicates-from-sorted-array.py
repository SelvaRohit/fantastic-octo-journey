nums = [0,0,1,1,1,2,2,2,3,3,4]
# for index,number in enumerate(nums):
i=0
while(i<len(nums)):
    print(nums)
    j=i+1
    while(j<len(nums)):
        # print(j)
        if(nums[i] == nums[j]):
            nums.remove(nums[j])
            j-=1
        j+=1
    i+=1
print(nums)