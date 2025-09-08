# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        elif not head.next.next:
            return head.next
        else:
            slow=head
            fast=head
            while fast != None and fast.next != None:
                slow=slow.next
                fast=fast.next.next
                # if fast == None or fast.next == None:
                #     return slow
                # elif fast.next == None:
            return slow


if __name__=="__main__":
    d=ListNode(4)
    c= ListNode(3,d)
    b=ListNode(2,c)
    a= ListNode(1,b)
