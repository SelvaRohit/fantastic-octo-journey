class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length=len(s)
        mid=length//2 if length%2 ==0 else (length//2)+1
        for i,current_element in enumerate(s[0:mid]):
            s[i],s[length-1-i]=s[length-1-i],current_element
            

if __name__ == "__main__":
    obj = Solution()
    s=list("selvas")
    obj.reverseString(s)
    print(s)