class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        m = len(matrix) # rows
        n = len(matrix[0]) # cols
    
        l = 0
        r = (m * n) - 1

        while l <= r: 

            mid = l + (r-l)//2

            row = mid // n
            col = mid % n

            mid_val = matrix[row][col]

            if mid_val > target:
                r = mid - 1
                
            elif mid_val < target:
                l = mid + 1

            elif mid_val == target:
                return True
        return False


    # Brute Force
        # return None # to avoid running code below this 
        #     for row in matrix:
        #         if target in row:
        #             return True

            # return False

        ###### O(m logn) 
        ## Find row, then binary search on row 

        # for row in matrix: 

        #     # correct row 
        #     if target >= row[0] and target <= row[-1]: 
        #         l = 0 
        #         r = len(row) - 1

        #         while l <= r:
        #             mid = l + (r-l)//2
        #             print(mid, row[mid])

        #             if row[mid] > target:
        #                 r = mid - 1
        #             elif row[mid] < target:
        #                 l = mid + 1
        #             elif row[mid] == target:
        #                 return True
        # return False