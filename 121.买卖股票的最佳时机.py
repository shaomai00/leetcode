# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for num in prices[1:]:
            max_profit = max(max_profit, num-min_price)
            if num < min_price:
                min_price = num
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    prices = [7,6,4,3,1]
    print(solution.maxProfit(prices))