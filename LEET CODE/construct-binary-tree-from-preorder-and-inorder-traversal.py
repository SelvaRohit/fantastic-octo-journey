# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    nextIndex=0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        root=TreeNode(preorder[0])
        def divide_build(start,end):
            # nonlocal nextIndex
            Solution.nextIndex+=1
            node=TreeNode(preorder[Solution.nextIndex])
            mid=inorder_map[preorder[Solution.nextIndex]]
            if end-start>1:
                node.left=divide_build(start,mid)
                node.right=divide_build(mid+1,end)
            return node
        if len(inorder)>2:
            inorder_map={}
            for i in range(len(inorder)):
                inorder_map[inorder[i]]=i
            mid=inorder_map[preorder[0]]
            root.left=divide_build(0,mid)
            root.right=divide_build(mid+1,len(inorder))
        # elif len(inorder)==1:
        #     root=TreeNode(preorder[0])
        elif len(inorder)==2:
            inorder_map={}
            for i in range(len(inorder)):
                inorder_map[inorder[i]]=i
            mid=inorder_map[preorder[0]]
            root.left=divide_build(0,mid)

        return root
if __name__ == "__main__":
    obj = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    preorder1=[-1]
    inorder1=[-1]
    preorder2=[1,2]
    inorder2=[2,1]
    root=obj.buildTree(preorder1,inorder1)
    def inorder_array(root):
        if root is None:
            return []
        return inorder_array(root.left) + [root.val] + inorder_array(root.right)

# Preorder Traversal (returns array)
    def preorder_array(root):
        if root is None:
            return []
        return [root.val] + preorder_array(root.left) + preorder_array(root.right)
    print(inorder_array(root))
    print(preorder_array(root))
