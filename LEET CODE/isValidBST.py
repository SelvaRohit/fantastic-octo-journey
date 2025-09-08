# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class InValidBST(Exception):
    """A simple custom exception."""
    pass

# Usage
# try:
#     raise CustomError("This is a custom error!")
# except CustomError as e:
#     print(f"Caught an error: {e}")

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkValidBST(root,acceptableRange):
            if root== None: # Base Condition
                return True
            root_val=root.val
            if acceptableRange[0]<root_val<acceptableRange[1]: # Check for within range and call the node recursively
                status_left=checkValidBST(root.left,[acceptableRange[0],root_val])
                status_right=checkValidBST(root.right,[root_val,acceptableRange[1]])
                return status_left and status_right
            else: # Not within the limits
                return False
        return checkValidBST(root,[float('-inf'),float('inf')])
if __name__ == "__main__":
    obj = Solution()
        # Tree:
    #     2
    #    / \
    #   3   1

    root_invalid = TreeNode(2)
    root_invalid.left = TreeNode(3)   # ❌ left child > root
    root_invalid.right = TreeNode(1)  # ❌ right child < root
        # Tree:
    #     2
    #    / \
    #   1   3

    root_valid = TreeNode(2)
    root_valid.left = TreeNode(1)
    root_valid.right = TreeNode(3)
    #Complex Cases
    root_complex_valid = TreeNode(8)
    root_complex_valid.left = TreeNode(4)
    root_complex_valid.right = TreeNode(12)

    root_complex_valid.left.left = TreeNode(2)
    root_complex_valid.left.right = TreeNode(6)

    root_complex_valid.right.left = TreeNode(10)
    root_complex_valid.right.right = TreeNode(14)

    # Tree:
#        8
#       / \
#      4   12
#     / \  / \
#    2  6 5  14
#         ^
#         ❌ violates BST: 5 < 8 but in right subtree of 8

    root_complex_invalid = TreeNode(8)
    root_complex_invalid.left = TreeNode(4)
    root_complex_invalid.right = TreeNode(12)

    root_complex_invalid.left.left = TreeNode(2)
    root_complex_invalid.left.right = TreeNode(6)

    root_complex_invalid.right.left = TreeNode(5)   # ❌ violates global BST rule
    root_complex_invalid.right.right = TreeNode(14)

    print(obj.isValidBST(root_complex_invalid))



        