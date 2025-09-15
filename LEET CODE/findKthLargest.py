class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k=len(nums)-k
        def quickselect(nums,k):
            p=0
            out=[nums[len(nums)-1]]
            for num in nums[0:len(nums)-1]:
                if num<=nums[len(nums)-1]:
                    out.insert(0,num)
                    p+=1
                else:
                    out.append(num)
            if p==k:
                return out[k]
            elif p>k:
                return quickselect(out[0:p],k)
            else:
                return quickselect(out[p+1:],k-p-1)
        return quickselect(nums,k)
if __name__ == "__main__":
    obj = Solution()
    nums=[3,2,1,5,6,4]
    print(obj.findKthLargest(nums,2))


