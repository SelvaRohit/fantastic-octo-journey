class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+((right-left)//2))
            # current_target=nums[left]+nums[mid]
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
if __name__=="__main__":
    obj=Solution()
    nums=[-1,0,3,5,9,12]
    target=2
    print(obj.search(nums,target))