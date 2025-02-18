nums=[0,0,1,1,1,2,2,3,3,4]
prev = None
write = 0
for i in nums:
    # print(nums)
    print(i)
    if prev == None or prev != i:
        nums[write] = i
        write += 1
    prev = i
print(nums)