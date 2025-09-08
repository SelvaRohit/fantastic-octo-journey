import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        out=[]
        for num in nums:
            heapq.heappush(out,-num)
        for i in range(k):
            output=heapq.heappop(out)
        return -output
if __name__ == "__main__":
    obj = Solution()
    arr=[3,2,1,5,6,4]
    print(obj.findKthLargest(arr,6))