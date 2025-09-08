class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        if (x[0]=='-'):
            sign=-1
            remaining=x[1:]
        elif (x[0]=='+'):
            sign =1
            remaining=x[1:]
        else:
            sign=1
            remaining=x
        # print(remaining[::-1])
        reversedNumber=sign*int(remaining[::-1])
        if (reversedNumber<(-(2**31)) or reversedNumber>((2**31)-1)):
            return 0
        else:
            return reversedNumber
sol=Solution()
print(sol.reverse("1563847412"))
        