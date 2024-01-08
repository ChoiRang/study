class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_color = colors[0]
        prev_time = neededTime[0]
        prev_cost, curr_cost = 0, 0
        for i in range(1, len(colors)):
            if colors[i] == prev_color:
                curr_cost = prev_cost + min(neededTime[i], prev_time)
                prev_time = max(neededTime[i], prev_time)
            else:
                curr_cost = prev_cost
                prev_color = colors[i]
                prev_time = neededTime[i]
            prev_cost = curr_cost

        return prev_cost
