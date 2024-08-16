class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # iterate thru each row, checking if number is less than greatest element in the row
        row = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                row = i
                break
            # elif matrix[i][-1] <= target:
            #     return False

        if row == -1:
            return False

        # Once we find the target row, binary search within said row 
        vals = matrix[row]
        
        l = 0
        r = len(vals) - 1

        while l <= r:
            print(l, r)
            m = (l + r) // 2

            if vals[m] < target:
                l = m + 1
            elif vals[m] > target: 
                r = m - 1
            else: # value found
                return True
        return False
