# Definition for a binary tree node.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # status = []
        def ismirror(Node1,Node2):
            if Node1.left != None and Node2.right !=None: 
                if Node1.left.val == Node2.right.val:
                    if Node1.left.val !=  None and Node2.right.val!=None:
                        ismirror(Node1.left,Node2.right)
                else:
                    raise StopIteration("False")
            elif Node1.left == None and Node2.right ==None:
                pass
            else :
                raise StopIteration("False")
            if Node1.right !=None and Node2.left !=None:
                if Node1.right.val == Node2.left.val:
                    if Node1.right.val != None and Node2.left.val != None:
                        ismirror(Node1.right,Node2.left)
                else:
                    raise StopIteration("False")
            elif Node1.right == None and Node2.left ==None:
                pass
            else :
                raise StopIteration("False")
        if root != None:
            if root.left != None and root.right !=None:
                try:
                    if root.left.val == root.right.val:
                        ismirror(root.left,root.right)
                    else:
                        return False
                    return True
                except StopIteration as e:
                    return False
            elif root.left == None and root.right ==None:
                return True
            else:
                return False
        else:
            return False
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
if __name__ == "__main__":
    obj = Solution()
    # Level 3
    node3_left = TreeNode(3)
    node4_left = TreeNode(4)
    node4_right = TreeNode(4)
    node3_right = TreeNode(3)

    # Level 2
    left_subtree = TreeNode(2, node3_left, node4_left)
    right_subtree = TreeNode(2, node4_right, node3_right)

    # Root
    symmetric_root = TreeNode(1, left_subtree, right_subtree)
    # Level 3
    left_child_3 = TreeNode(3)
    right_child_3 = TreeNode(3)

    # Level 2
    left_subtree = TreeNode(2, None, left_child_3)
    right_subtree = TreeNode(2, None, right_child_3)

    # Root
    non_symmetric_root = TreeNode(1, left_subtree, right_subtree)
    left_leaf = TreeNode(3)
    right_leaf = TreeNode(3)

    # Level 2
    left_child = TreeNode(2, left_leaf, None)
    right_child = TreeNode(2, None, right_leaf)

    # Root
    tri_root = TreeNode(1, left_child, right_child)
    # Level 4
    left_deep = TreeNode(13)
    right_deep = TreeNode(13)

    # Level 3
    left_76 = TreeNode(76, None, left_deep)
    right_76 = TreeNode(76, None, right_deep)

    # Level 2
    left_node = TreeNode(-42, None, left_76)
    right_node = TreeNode(-42, right_76, None)

    # Root
    non_tri_root = TreeNode(9, left_node, right_node)

    print (obj.isSymmetric(non_tri_root))
            