n=38
nums=[0,1]
if(n in nums):
    print(n)
else:
    for i in range(n-1):
        nums.append(nums[i]+nums[i+1])
    print (nums[-1])
