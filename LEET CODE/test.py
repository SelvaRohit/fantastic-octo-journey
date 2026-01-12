class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        while n:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

if __name__ == "__main__":
    obj=Solution()
    node7=ListNode(7)
    node6 = ListNode(6,node7)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)
    obj.removeNthFromEnd(head,5)
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next