class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_sorted_lists(list1, list2):
    dummy = ListNode(-1)  # Temporary dummy node to start the merged list
    current = dummy   # Pointer to build the new list

    # Merge while both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining part of the list that is not empty
    current.next = list1 if list1 else list2

    return dummy.next