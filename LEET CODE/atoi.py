class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        import numpy as np
        s=s.lstrip()
        try:
            if (s[0]=='-' or s[0]=='+'):
                sign=s[0]
                remaining=s[1:]
            else:
                sign='+'
                remaining=s
            pattern = re.compile("[0-9]")
            Number=''
            for each_character in remaining:
                if pattern.match(each_character):
                    Number+=each_character
                elif (each_character==""):
                        continue
                else:
                    break

            try:
                value=int(sign+Number)
                if value<(-(2**31)):
                    # print(5)
                    return (-(2**31))
                elif value>((2**31)-1):
                    # print(6)
                    return ((2**31)-1)
                else:
                    return value
            except:
                # raise 
                return (0)
        except IndexError:
            return 0
if __name__=="__main__":
    S=Solution()
    inp="-91283472332"
    print(S.myAtoi(inp))