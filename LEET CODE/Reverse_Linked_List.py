# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head:
           current = head
           prev=None
           while current:
                temp=current.next
                current.next=prev
                prev=current
                current=temp
           return prev 


if __name__=="__main__":
    d=ListNode(4)
    c= ListNode(3,d)
    b=ListNode(2,c)
    a= ListNode(1,b)
    print(d)
    # a.next=b
    # b.next=c
    # c.next=d
    obj=Solution()
    _out=(obj.reverseList(a))
    print(_out)
    # while _out != None:
    #     print(_out)
    #     _out=_out.next