# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if list1 is None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        else:
            while list1 is not None:
                stack.append(list1.val)
                list1 = list1.next
            while list2 is not None:
                stack.append(list2.val)
                list2 = list2.next
            stack.sort()

            dummy = ListNode(0)
            result = dummy
            for val in stack:
                result.next = ListNode(val)
                result = result.next
            return dummy.next