class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list1=[]
        divisor=10
        quotient=1
        rem=0
        if (x<=-1):
            return False
        else:
            while (rem != x):
                rem=(x%divisor)//quotient
                list1.append(rem)
                rem=(x%divisor)
                quotient=divisor
                divisor=divisor*10
                # print("hh")
            print(list1)
            reversed_list1=list1
            list1.reverse()
            print(list1)
            print(reversed_list1)
            if (list1==reversed_list1):
                return True
            else:
                return False

c1=Solution()
u=123
pal=c1.isPalindrome(u)
print(pal)        



