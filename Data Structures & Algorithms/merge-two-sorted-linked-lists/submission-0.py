# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode()
        dummy = merge
        head_1 = list1
        head_2 = list2
        while head_1 != None and head_2 != None:
            if head_1.val <= head_2.val:
                merge.next = head_1
                head_1 = head_1.next
                merge = merge.next
            elif head_2.val <= head_1.val:
                merge.next = head_2
                head_2 = head_2.next
                merge = merge.next
        merge.next = head_1 or head_2
        return dummy.next


        