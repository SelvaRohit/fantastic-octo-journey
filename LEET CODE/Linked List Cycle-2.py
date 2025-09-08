class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        if head !=None and head.next != None and head.next.next != None:
            while slow != None and fast !=None:
                try:
                    slow=slow.next
                    fast=fast.next.next
                    if slow==fast:
                        return True
                except AttributeError:
                    return False
        return False


if __name__=="__main__":
    
    c=ListNode(2)
    b=ListNode(2,c)
    a=ListNode(3,b)
    root=ListNode(1,a)
    obj1=Solution()
    print(obj1.hasCycle(root))        