class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=1
        prefix_array=[1]
        postfix=1
        postfix_array=[1]
        answer=[]
        for i in range(len(nums)):
            prefix*=nums[i]
            prefix_array.append(prefix)
            postfix*=nums[-(i+1)]
            postfix_array.append(postfix)
        postfix_array=postfix_array[::-1]
        # print(prefix_array)
        # print(postfix_array)
        return[prefix_array[i]*postfix_array[i+1] for i in range(len(nums))]
        return answer
if __name__ == "__main__":
    obj = Solution()
    arr=[1,2,3,4]
    print(obj.productExceptSelf(arr))
            