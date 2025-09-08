# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter=0
        if root != None:
            self.traversal(root)
            return(self.diameter)
        return 0

    # @staticmethod
    def traversal(self,Node):
        if Node == None:
            return 0
        left_depth=self.traversal(Node.left)
        right_depth=self.traversal(Node.right)
        curr_dia= left_depth+right_depth
        # Solution.diameter=max(Solution.diameter,curr_dia)
        if self.diameter < curr_dia:
            self.diameter=curr_dia
        return 1+max(left_depth,right_depth)
if __name__ == "__main__":
    obj = Solution()
    a=b=c=d=None
    # a=TreeNode(15)
    # b=TreeNode(7)
    # c=TreeNode(20)
    # d=TreeNode(9)
    e= TreeNode(1)
    # f=TreeNode(3,c,d)
    root=TreeNode(55,e)
    # root=None
    print(obj.diameterOfBinaryTree(root))