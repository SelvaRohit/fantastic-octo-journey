class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_element=nums[0]
        count=0
        for i in nums:
            if count==0:
                maj_element=i
            if i == maj_element:
                count+=1
            else:
                count-=1
        return maj_element
if __name__=="__main__":
    lis1=[1,2,1,3,1,1]
    obj=Solution()
    print(obj.majorityElement(lis1))