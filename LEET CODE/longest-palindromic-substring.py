from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=j=mid=len(s)//2
        print(type(i),type(j),type(mid))
        max_palindrome=defaultdict(list)
        while (i>-1):
            odd_s1=s[mid:j+2]
            odd_s2=s[i-1:mid+1]
            even_s=s[i-1:j+2]
            if s[mid:(j+2)] == s[mid:j+2:-1]:
                max_palindrome[len(s[mid:j+2])]=max_palindrome[len(s[mid:j+2])].append(s[mid:j+2])
            elif s[(i-1):(mid+1)] == s[i-1:mid+1:-1]:
                max_palindrome[len(s[i-1:mid+1])]=max_palindrome[len(s[i-1:mid+1])].append(s[i-1:mid+1])
            elif even_s == even_s[::-1]:
                max_palindrome[len(s[i-1:j+2])]=max_palindrome[len(s[i-1:j+2])].append(s[i-1:j+2])
            i-=1
            j+=1
        return max_palindrome.keys()
if __name__ == "__main__":
    obj = Solution()
    pal="xbabx1"
    a=obj.longestPalindrome(pal)
    print(a)