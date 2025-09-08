class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        previous_steps={1:2,2:1}
        if n==1 or n==2:
            return previous_steps[n]
        out=0
        for i in range(3,n+1):
            one_way=i-1
            other_way=i-2
            out=(previous_steps[one_way]+previous_steps[other_way])
            previous_steps[i]=out
        
        return out
if __name__ == "__main__":
    obj = Solution()
    steps=3
    print(obj.climbStairs(steps))