# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        ## Iterative 
        
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else: 
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2 # when one list is complete, autofill with remainder of the other

        return dummy.next 

        # Recursive

        # Base cases: one list is empty
        # if list1 is None: 
        #     return list2
        # if list2 is None: 
        #     return list1

        # if list1.val <= list2.val: 
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     lsit2.next = self.merge(twoLists(list2.next, list1))
        #     return list2
