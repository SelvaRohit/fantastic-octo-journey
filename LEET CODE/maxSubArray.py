class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum=nums[0]
        max_sum=nums[0]
        if len(nums)==1:
            return current_sum
        else:
            for num in nums[1:]:
                current_sum=max(num,num+current_sum)
                max_sum=max(current_sum,max_sum)
            return max_sum
if __name__ == "__main__":
    obj = Solution()
    array=[-2,1,-3,4,-1,2,1,-5,4]
    print(obj.maxSubArray(array))