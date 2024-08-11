class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # return len(set(nums)) != len(nums)

        map = {}
        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1

        return False