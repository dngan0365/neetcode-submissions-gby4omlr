class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        daySet = set(days)
        memo = {}

        def dfs(day):

            if day > days[-1]:
                return 0

            if day in memo:
                return memo[day]

            if day in daySet:

                memo[day] = min(
                    costs[0] + dfs(day + 1),
                    costs[1] + dfs(day + 7),
                    costs[2] + dfs(day + 30)
                )

            else:
                memo[day] = dfs(day + 1)

            return memo[day]

        return dfs(days[0])