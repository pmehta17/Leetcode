class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-1 * num for num in nums]
        heapq.heapify(maxHeap)
        

        for i in range(k):
            x = heapq.heappop(maxHeap)
            if i == k - 1:
                return x * -1