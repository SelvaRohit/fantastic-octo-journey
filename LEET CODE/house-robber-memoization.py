import time
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)//2):
        if len(nums)==1:
            return nums[0]
        else:
            i=0
            j=1
            memoization={}
            def maxAmountHouse(curr_index):
                if curr_index>=len(nums):
                    return 0
                elif curr_index in memoization:
                    return memoization[curr_index]
                else:
                    firstHouse=maxAmountHouse(curr_index+2)
                    memoization[curr_index+2]=firstHouse
                    secondHouse=maxAmountHouse(curr_index+3)
                    memoization[curr_index+3]=secondHouse
                return nums[curr_index]+max(firstHouse,secondHouse)
            return max(maxAmountHouse(0),maxAmountHouse(1))
if __name__ == "__main__":
    obj = Solution()
    arr=[1,2,3,1]
    arr1=[2,7,9,3,1]
    arr2=[2,1,1,2]
    arr3=[226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
    # st=time.time()
    print(obj.rob(arr3))
    # print(time.time()-st)