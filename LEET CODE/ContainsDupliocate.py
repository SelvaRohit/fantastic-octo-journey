class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map={}
        for num in nums:
            dup=hash_map.setdefault(num,0)
            hash_map[num]=dup+1
            if hash_map[num]>1:
                return True
        return False
if __name__ == "__main__":
    obj = Solution()
    arr=[1,1,1,3,3,4,3,2,4,2]
    arr1=[1,2,3,4]
    arr2=[1,2,3,1]
    print(obj.containsDuplicate(arr))