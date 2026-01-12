# Definition for singly-linked list.
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
        if head.next != None:
            slow= head
            fast=head.next
            i=1
            while fast != None:
                if fast.next != None:
                    if fast.next.next != None:
                        fast=fast.next.next
                    else:
                        i=(i*2)+1

                        break
                        # pass
                else:
                    # slow=slow.next
                    # i+=1
                    i=i*2
                    break
                    # pass
                slow=slow.next
                i+=1
                
            if n==i:
                head=head.next
            else:
                n=i-n+1
                if i//2 <n:
                    start=slow
                    n=n-(i//2)-1
                else:
                    start=head
                    n=n-2
                for _ in range(n):
                    start=start.next
                start.next=start.next.next

if __name__ == "__main__":
    obj=Solution()
    node7=ListNode(7)
    node6 = ListNode(6,node7)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)
    obj.removeNthFromEnd(head,7)
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next