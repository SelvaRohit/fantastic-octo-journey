class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maximum_or=nums[len(nums)-1]
        i=0
        j=1
        answer=[]
        last_answer=0
        while i<len(nums):
            # if nums[i] >= maximum_or:
            #     answer.append(1)
            #     i +=1
            #     j =i+1
            if nums[i]|nums[j]|last_answer >= maximum_or:
                answer.append(j-i+1)
                last_answer=0
                i +=1
                j =i+1

            else:
                last_answer = last_answer|nums[j]
                j+=1
        return answer
if __name__ == "__main__":
    obj = Solution()
    arr1=[1,0,2,1,3]
    arr2=[1,2]
    arr3=[8,10,8]
    print(obj.smallestSubarrays(arr3))

