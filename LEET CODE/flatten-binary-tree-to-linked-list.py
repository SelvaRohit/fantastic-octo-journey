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
        def linkedlist(root):
            curr_node=TreeNode(root.val)
            if root.left is not None:
                curr_node.right=linkedlist(root.left)
            if root.right is not None:
                Solution.last_node.pop().right=linkedlist(root.right)
            Solution.last_node.append(curr_node)
            return curr_node
        if root is not None and root.left is not None:
            node = linkedlist(root.left)
            # print(root)
            # return root
            root.left=None
            root.right=node
            # return root
        else:
            return None
if __name__ == "__main__":
    obj = Solution()
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    # root.right.left = None   # since array has None here
    root.right.right = TreeNode(6)
    print(root)
    print(obj.flatten(root))
    def preorder(node):
        if node is not None:
            print(node.val)
            preorder(node.left)
            preorder(node.right)
    preorder(root)