class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # ans = [0] * k
        # max_heap = [] 

        # ct = Counter(nums)

        # for num, freq in ct.items(): 
            
        #     heapq.heappush(max_heap, [-1*freq, num])

        #     if len(heap) > k: 
        #         heapq.heappop(max_heap)
        
        # for i in range(k):
        #     ans[i] = heapq.heappop(max_heap)[1]

        # return ans

        min_heap = []
        ct = Counter(nums)

        for num, freq in ct.items():
            heapq.heappush(min_heap, [freq, num])

            if len(min_heap) > k: 
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]
            