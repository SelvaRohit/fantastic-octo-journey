# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        Code is done with append all the elements in the order
        of left to right
        """
        if root:
            mode=0
            queue=[root]
            out=[]
            while queue:
                n=len(queue)
                level=[]
                for i in range(n):
                    node=queue.pop(0)
                    level.append(node.val)
                    if  node.left:
                        queue.append(node.left)
                    if  node.right:
                        queue.append(node.right)
                if mode:
                    level.reverse()
                    mode=0
                else:
                    mode=1
                out.append(level)
            return out
        return []
if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(6)
    root3 = TreeNode(10)
    root3.left = TreeNode(5)
    root3.right = TreeNode(15)
    root3.left.left = TreeNode(2)
    root3.left.right = TreeNode(7)
    root3.left.right.left = TreeNode(6)
    root3.right.right = TreeNode(20)
    root4=None
    print(obj.zigzagLevelOrder(root4))
        