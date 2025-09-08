class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
obj=Solution()
colours=[2,0,2,1,1,0]
print(obj.sortColors(colours))