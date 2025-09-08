# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.createBST(nums,0,len(nums)-1)

    def createBST(self,nums,left,right):
        
        if right<left:
            return None
        mid=(left+right)//2
        # element=nums[mid]
        left_node=self.createBST(nums,left,mid-1)
        right_node=self.createBST(nums,mid+1 ,right)
        return TreeNode(nums[mid],left=left_node,right=right_node)  
if __name__ == "__main__":
    # obj = Solution()``
    def inorder_traversal(root):
        if not root:
            return []
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Test code:
    sol = Solution()
    root = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(inorder_traversal(root))
    # print(obj.sortedArrayToBST(numm))

        