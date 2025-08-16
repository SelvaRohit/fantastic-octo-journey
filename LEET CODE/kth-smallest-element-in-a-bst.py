# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        bst=[]
        self.out=None
        # global stop
        self.stop=False
        def inordertraversal(node):
            # nonlocal stop,out
            if node is None or self.stop:
                return None


            else:
                inordertraversal(node.left)
                bst.append(node.val)
                if len(bst)>=k:
                    # return bst
                    self.out=bst[k-1]
                    self.stop=True
                inordertraversal(node.right)
        inordertraversal(root)
        return self.out
        # print(bst)
        # return bst[k-1]
def build_bst(start, end):
    """Builds a balanced BST from values in [start, end]."""
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = TreeNode(mid)
    
    root.left = build_bst(start, mid - 1)
    root.right = build_bst(mid + 1, end)
    
    return root


# Build BST with values 1–20
root1_20 = build_bst(1, 20)
if __name__ == "__main__":
    obj = Solution()
    print(obj.kthSmallest(root1_20,4))
