class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i,j in enumerate(nums2): #Worst case Loop will run for all the elements in Nums2 
            start=0 #Binary Search Start index
            end=m+i-1
            if(j>=nums1[end]):
                nums1[end+1:]=nums2[i:]
                break
            elif(j<=nums1[start]):
                nums1=nums2[0:n]+nums1[0:m]
                break
            else:
                while(end>=start):
                    mid = start + ((end-start)//2)
                    if(j==nums1[mid]):
                        break
                    elif(j<nums1[mid]):
                        end=mid-1
                    else:
                        start = mid+1
                nums1.pop()
                nums1.insert(mid,j)
        return nums1

        