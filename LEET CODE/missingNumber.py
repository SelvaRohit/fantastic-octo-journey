class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=len(nums)
        expected_sum = (count*(count+1))/2
        actual_sum = sum(nums)
        return int(expected_sum-actual_sum)
if __name__=="__main__":
    obj=Solution()
    lis1=[3,0,1]
    print((obj.missingNumber(lis1)))
        