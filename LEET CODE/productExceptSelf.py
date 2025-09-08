import numpy as np
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            prefix=np.prod(nums[i+1::])
            suffix=np.prod(nums[0:i])
            result.append(int(prefix*suffix))
        return result
if __name__ == "__main__":
    obj = Solution()
    arr=[1,2,3,4]
    print(obj.productExceptSelf(arr))