class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end=len(nums)-1
        if end==1:
            if nums[start]+nums[end]==target:
                return start+1,end+1
        else:
            while start<=end:
                mid=start+(end-start)//2
                sumation=nums[start]+nums[mid]
                if sumation==target:
                    return start+1,mid+1
                elif sumation<target:
                    start=mid
                else:
                    end=mid
obj=Solution()
l1=[-1,0]
target=-1
print(obj.twoSum(l1,target))