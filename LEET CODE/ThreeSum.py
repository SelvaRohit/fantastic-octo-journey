class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        for i in range(len(nums)):
            heap={}
            target=(0-nums[i])
            for j in range(len(nums)-i):
                currentindex=j+i
                if nums[currentindex] not in heap:
                    heap[target-nums[currentindex]]=currentindex
                else:
                    output.append([i,heap[target-nums[currentindex]],currentindex])
        # return None,None,None #if not a any 3 numbers sum is equal to target
obj=Solution()
nums=[-1,0,1,2,-1,-4]
print(obj.threeSum(nums))

        
