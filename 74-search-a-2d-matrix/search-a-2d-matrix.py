class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        ROWS, COLS = len(matrix), len(matrix[0])
        top = 0
        bot = ROWS - 1

        # edge cases, targtet is larger/smaller than all values in array
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False


        while top <= bot: 

            row = top + (bot - top) // 2

            if target > matrix[row][-1]: 
                top = row + 1
            elif target < matrix[row][0]: 
                bot = row - 1


            else: # right row 
                
                nums = matrix[row]
                l = 0
                r = COLS - 1

                while l <= r: 
                    m = l + (r-l) //2

                    if nums[m] < target:
                        l = m + 1
                    elif nums[m] > target:
                        r = m - 1
                    else:
                        return True
                return False
        return False



        # ## Brute Force approach 
        # for row in matrix:
        #     if target in row:
        #         return True

        # return False