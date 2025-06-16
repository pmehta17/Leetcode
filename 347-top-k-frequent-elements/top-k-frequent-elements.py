class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # 1. add numbers to hashamap
        freq_map = Counter(nums)
        print(freq_map)


        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = [] 
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans