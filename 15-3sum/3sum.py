class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for `i`

            j = i + 1
            k = len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    # Skip duplicates for `j` and `k`
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif cur_sum > 0:
                    k -= 1
                else:
                    j += 1

        return list(ans)  # Convert the set to a list before returning


        ## Time complexity: O(n log n ) because we are sorting