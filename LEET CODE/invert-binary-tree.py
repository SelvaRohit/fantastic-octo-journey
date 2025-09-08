# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]

        """
        invertTree_rec(root)
        return root
def invertTree_rec(root):
    if root !=None:
            
        if root.left != None:
                invertTree_rec(root.left)
        if root.right != None:
                invertTree_rec(root.right)
        root.left,root.right=root.right,root.left
if __name__=="__main__":
    # print(2)
    a=TreeNode(1)
    b=TreeNode(3)
    c=TreeNode(6)
    d=TreeNode(9)
    e=TreeNode(2,a,b)
    f=TreeNode(7,c,d)
    root=TreeNode(5,e,f)
    obj1=Solution()
    print(obj1.invertTree(root))
    