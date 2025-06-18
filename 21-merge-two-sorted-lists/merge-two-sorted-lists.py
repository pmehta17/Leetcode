# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list ans 

        dummy = ListNode()
        tail = dummy 

        # compare head of list1 and list2
        while list1 and list2: 
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
        
            tail = tail.next
        
        tail.next = list1 if list1 else list2

        return dummy.next

        # add smaller to ans, remove from original list 

        # repeat until list1 and list2 empty 
