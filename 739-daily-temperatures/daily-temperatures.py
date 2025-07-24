class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        
        stack = []

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()

                # update ans
                ans[stackIdx] = i - stackIdx

            stack.append([t, i])

        return ans



        # # two pointer solution 
        # l = 0 
        # r = l + 1

        # ans = [0] * len(temperatures)

        # while l < len(temperatures):

        #     while r < len(temperatures) and temperatures[r] <= temperatures[l]:
        #         r += 1
        #         print(l, r)
        #     if r < len(temperatures):  # found a warmer day
        #         ans[l] = r - l
        #     # else:
        #     #     ans[l] = 0
        #     l += 1
        #     r = l + 1
        # return ans

            