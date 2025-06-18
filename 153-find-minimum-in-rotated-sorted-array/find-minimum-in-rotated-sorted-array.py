class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotating the array means moving the last element to the beginning 
        # rotating [1 2 3 4 5] twice would become [5 1 2 3 4] and then [4 5 1 2 3]
        # goal: find min in log(n) time 

        # l = 0 
        # r = len(nums) - 1

        # mid = l + (r-l)/2
        return min(nums)



        