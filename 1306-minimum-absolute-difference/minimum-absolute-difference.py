class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        min_diff = float("inf")

        ans = []


        arr.sort()

        for i in range(1, len(arr)): 
            d = arr[i] - arr[i - 1]
            
            if d == min_diff: 
                l = [arr[i-1], arr[i]]
                ans.append(l)

            if d < min_diff: 
                ans.clear()
                ans.append([arr[i-1], arr[i]])
                min_diff = d
            


        return ans