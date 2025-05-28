from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        min_count = len(nums) // 3

        ans = []

        count = Counter(nums)
        # print(count)

        for k, v in count.items():
            if v > min_count:
                ans.append(k)
        return ans

        