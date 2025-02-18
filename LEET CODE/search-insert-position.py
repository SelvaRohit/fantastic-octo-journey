nums = [1,3,4,7,9]
target = 8
if(nums[0]>target):
    out = 0
elif (nums[-1]<target):
    out=len(nums)
else:
    out=-1
    left,right = 0,len(nums)-1
    while(left<=right):
        mid=((right-left+1)//2)+left
        # print(mid)
        # mid = ((right-left+1)%2)==1?
        if(nums[mid]==target):
            out=mid
            break
        elif(nums[mid]<target):
            left=mid+1
        else:
            right=mid-1
    if (out==-1):
        print(f" Not in list {mid}")
        out = (mid,mid+1)[nums[mid]<target]
    # else:
    #     print(f"Found {out}")
    # print(mid)
    # print(left)
    # print(right)
print(out)