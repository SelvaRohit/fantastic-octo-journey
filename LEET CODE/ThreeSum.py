class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(len(nums)):
            heap={}
            target=(0-nums[i])
            for j in range(len(nums)-i):
                currentindex=j+i
                if nums[currentindex] not in heap:
                    heap[nums[currentindex]]=currentindex
                
        
