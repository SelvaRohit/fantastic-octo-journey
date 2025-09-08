class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        out=""
        for i in range(len(strs[0])):
            if (strs[0][i] == strs[-1][i]):
                out+=strs[0][i]
            else:
                break
        return(out)
obj=Solution()
inp=["flower","flow","flight"]
print(obj.longestCommonPrefix(inp))