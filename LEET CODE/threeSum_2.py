class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums=list(set(    nums))
        nums.sort()
        out=[]
        last_element=None
        for i,curr in enumerate(nums):
            low=i+1
            high=len(nums)-1
            # target=-(curr)
            if last_element==None or last_element!=curr:
                last_low=None
                last_high=None

                while (low<high):
                    # if last_high!=nums[high] or last_low!=nums[low]:
                    if len(out)==0 or out[-1]==[curr,nums[low],nums[high]]:
                        '''This condition is to avoid the operation 
                            if last iteration and current iteration carrys same numbers
                        '''  
                        last_low=nums[low]
                        last_high=nums[high]
                        target=curr+nums[low]+nums[high]
                        if target==0:
                            out.append([curr,nums[low],nums[high]])
                            low+=1
                            high-=1
                            # break
                        elif target>0:
                            high-=1
                        else:
                            low+=1
                    else:
                        last_low=nums[low]
                        last_high=nums[high]
                        low+=1
                        high-=1
            last_element=curr
        return out
if __name__ == "__main__":
    obj = Solution()
    arr=[-1,0,1,2,-1,-4]
    arr1=[0,0,0,0]
    arr2=[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    print(obj.threeSum(arr2))
        