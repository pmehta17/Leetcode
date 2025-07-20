class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        ans = []



        while matrix: 
            
            # row 1 (l to r)
            ans.extend(matrix.pop(0))


            # last col (top to bottom)
            for row in matrix: 
                if row: 
                    ans.append(row.pop(-1))


            # last row (r to l)
            if matrix: 
                ans.extend(matrix.pop(-1)[::-1])
  

            # first col (bottom to top)
            for row in reversed(matrix):
                if row: 
                    ans.append(row.pop(0))

        
        return ans

        