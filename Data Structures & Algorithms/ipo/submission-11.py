class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        done = set()
        for i in range(k):
            limit_capital = set()
            for j in range(len(capital)):
                if (capital[j] <= w) and (j not in done):
                    print("order: ", j, "capital ", capital[j])
                    limit_capital.add(j)
            print(limit_capital)
            if len(limit_capital) != 0:
                max_profit = -999
                max_order = -1
                for p in limit_capital:
                    if max_profit < profits[p]:
                        max_profit = profits[p]
                        max_order = p
                print(i, " profit: ", max_profit)
                done.add(max_order)
                w += max_profit
            else:
                return w
        return w
             
