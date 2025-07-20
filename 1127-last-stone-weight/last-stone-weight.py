class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)


        while len(heap) >= 2: 
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1

            diff = abs(x - y)

            if diff == 0:
                continue
            else:
                heapq.heappush(heap, -1 * diff)

        return -1 * heap[0] if heap else 0

