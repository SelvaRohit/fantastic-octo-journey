class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_freq={}
        majority=len(nums)/2
        for i in nums:
            element_freq.update({i:element_freq.get(i,0)+1})
            if element_freq[i] > majority:
                return i
        return None
