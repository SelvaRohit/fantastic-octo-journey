class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) ==1:
            return [[nums[0]]]
        permutations=self.permute(nums[1:])
        out=[]
        for p in permutations:
            index=0
            for _ in range(len(p)+1):
                p_copy=p.copy()
                p_copy.insert(index,nums[0])
                out.append(p_copy)
                index+=1
        return out

if __name__=='__main__':
    nums=[1,2,3]
    obj=Solution()
    a=obj.permute(nums)
    print(a)