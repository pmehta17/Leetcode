class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = [0] * k
        ct = Counter(nums)

        max_heap = []   

        for num, freq in ct.items(): 
            heapq.heappush(max_heap, [-1*freq, num])
        
        for i in range(k):
            ans[i] = heapq.heappop(max_heap)[1]

        return ans
       
       

            