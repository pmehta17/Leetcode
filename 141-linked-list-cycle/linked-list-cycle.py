# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        # method 1: hashset to keep track of visited nodes
        # Time complexity: O(n)
        # Space complexity: O(n)

        # seen = set()
        # curr = head

        # while curr: 
        #     if curr in seen:
        #         return True # cycle; revisiting same node again
        #     seen.add(curr) # add node to set
        #     curr = curr.next # move to next node 
        # return False

        # Method 2: Fast and slow Pointer 
        # Time complexity: O(n)
        # Space complexity: O(1)

        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return True


            




