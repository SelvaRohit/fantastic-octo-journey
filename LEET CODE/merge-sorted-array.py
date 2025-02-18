nums1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 0
nums2 = [-50,-50,-48,-47,-44,-44,-37,-35,-35,-32,-32,-31,-29,-29,-28,-26,-24,-23,-23,-21,-20,-19,-17,-15,-14,-12,-12,-11,-10,-9,-8,-5,-2,-2,1,1,3,4,4,7,7,7,9,10,11,12,14,16,17,18,21,21,24,31,33,34,35,36,41,41,46,48,48]
n = 63
if(m==0):
    nums1[0:n]=nums2
else:
    for i,j in enumerate(nums2): #Worst case Loop will run for all the elements in Nums2 
        start=0 #Binary Search Start index
        end=m+i-1
        if(j>=nums1[end]):
            nums1[end+1:]=nums2[i:]
            break
        elif(j<=nums1[start] and nums2[n-1]<=nums1[start]):
            nums1=nums2[i:n]+nums1[0:m]
            break
        else:
            while(end>=start):
                mid = start + ((end-start+1)//2)
                if(j==nums1[mid]):
                    break
                elif(j<nums1[mid]):
                    end=mid-1
                else:
                    start = mid+1
            nums1.pop()
            mid=(mid,mid+1)[nums1[mid]<j]
            nums1.insert(mid,j)
print(nums1)
        
           
            