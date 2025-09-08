class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums=list(set(    nums))
        nums.sort()
        out=set()
        last_element=None
        for i,curr in enumerate(nums):
            if last_element == None or last_element!=curr:
                target=-(curr)
                hashmap={}
                for j in range(i+1,len(nums)):
                    if nums[j] in hashmap:
                        out.add((curr,nums[hashmap[nums[j]]],nums[j]))

                    else:
                        found=target-nums[j]
                        hashmap[found]=j
                last_element=curr
        out=list(out)
        output=[]
        for triplet in out:
            output.append(list(triplet))
        return output
if __name__ == "__main__":
    obj = Solution()
    arr=[-1,0,1,2,-1,-4]
    print(obj.threeSum(arr))
        