from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)] # index represents frequency, array at that index represents numbers with that frequency

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)


        ans = []
        for i in range(len(freq) -1, 0, -1): # Iterate in reverse order
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

    # O(n)