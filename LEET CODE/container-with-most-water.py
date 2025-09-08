class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1,p2=0,len(height)-1
        maximumArea=0
        while(p1<p2):
            currentArea=((p2-p1)*min(height[p1],height[p2]))
            if maximumArea<currentArea:
                maximumArea=currentArea
                # max[1]=p1
                # max[2]=p2
            if (height[p1]<height[p2]):
                p1+=1
            else:
                p2-=1
        return(maximumArea)
obj=Solution()
Height=[1,8,6,2,5,4,8,3,7]
print(obj.maxArea(Height))

