from typing import List
class Solution(object):
    def __init__(self):
        self.generatedParanthesis=[[]]
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        allComb=[[]]
        recursiveParanthesis([1],allComb)
        print(f"Answer:{allComb}")
def recursiveParanthesis(currentComb:List[int],generatedParanthesis:List[List[int]]):
    print(currentComb)
    for i in range(2):
        if i==0:
            currentComb.append(1)
            if sum(currentComb)>3:
                currentComb.pop()
                continue
        else:
            currentComb.append(-1)
            if sum(currentComb)<0:
                currentComb.pop()
                continue
        if (sum(currentComb)==0):
            generatedParanthesis.append(currentComb)
        else:
            recursiveParanthesis(currentComb,generatedParanthesis)
            # pass
obj=Solution()
obj.generateParenthesis(3)