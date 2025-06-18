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

        seen = set()
        curr = head

        while curr: 
            if curr in seen:
                return True # cycle; revisiting same node again
            seen.add(curr) 
            curr = curr.next
        return False

            




