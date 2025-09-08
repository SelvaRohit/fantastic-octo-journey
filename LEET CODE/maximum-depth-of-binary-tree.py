# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        out=0
        if root != None:
            out=traversal(root)
        return out
def traversal(root):
    if root==None:
        return 0
    left_dpeth=traversal(root.left)
    right_depth=traversal(root.right)
    return 1+max(left_dpeth,right_depth)
if __name__=="__main__":
    a=TreeNode(15)
    b=TreeNode(7)
    c=TreeNode(20,a)
    d=TreeNode(9,None,b)
    root=TreeNode(12,c,d)
    obj=Solution()
    print(obj.maxDepth(root))
