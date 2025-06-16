class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # set doesn't allow for duplicates.

        s = set(nums)
        return len(s) != len(nums)
        