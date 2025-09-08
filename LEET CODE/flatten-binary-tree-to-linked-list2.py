class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    last_node=[]
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes=[]
        def preordertraversal(node):
            if node:
                nodes.append(node)
                preordertraversal(node.left)
                preordertraversal(node.right)
        preordertraversal(root)
        if len(nodes)>1:
            index=0
            while index+1<len(nodes):
                nodes[index].left=None
                nodes[index].right=nodes[index+1]
                index+=1
            else:
                nodes[-1].left=None
                nodes[-1].right=None
if __name__ == "__main__":
    obj = Solution()
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    # root.right.left = None   # since array has None here
    root.right.right = TreeNode(6)
    # print(root)
    # print(obj.flatten(root))
    obj.flatten(root)
    def preorder(node):
        if node is not None:
            print(node.val)
            preorder(node.left)
            preorder(node.right)
    preorder(root)            


