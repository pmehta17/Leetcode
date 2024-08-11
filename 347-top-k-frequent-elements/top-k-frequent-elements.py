from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        freq_map = defaultdict(int) # key: number; value: frequency

        for num in nums:
            freq_map[num] += 1
            
        sorted_freq_map = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)

        ans = []

        print(sorted_freq_map)
        for i in range(k):
            ans.append(sorted_freq_map[i][0])
            print(sorted_freq_map[i][0])
            
        return ans