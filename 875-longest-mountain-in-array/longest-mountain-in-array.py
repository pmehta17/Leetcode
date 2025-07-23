class Solution:
    def longestMountain(self, arr: List[int]) -> int:


        max_length = 0

        # find local max indexes
        for i in range(1, len(arr) - 1):

            temp_len = 0

            
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

                l, r = i, i
                
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1

                while r < len(arr) - 1 and arr[r + 1] < arr[r]:
                    r += 1

                max_length = max(max_length, r - l + 1)
        return max_length
                

                
            