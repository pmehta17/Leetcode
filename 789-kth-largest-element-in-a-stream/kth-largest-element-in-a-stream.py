class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap) ## modifies in place; do not set var equal to this

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        

    def add(self, val: int) -> int:

        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # only pop if we have more than k elements in our heap
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)