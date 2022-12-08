# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
from typing import List
class Solution:
    # 对于每个位置，左边的最高和右边的最高的，选矮的那一个，减去当前自己的高度，就是这个位置能接的水量
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = []
        # 先一遍遍历左边最高
        max_height = -1
        for cur_height in height:
            leftmax.append(max_height)
            max_height = max(cur_height, max_height)
        # 再逆向遍历一下右边最高
        max_height = -1
        for cur_height in height[::-1]:
            rightmax = [max_height] + rightmax
            max_height = max(cur_height, max_height)
        sum_height = 0
        for l,h,r in zip(leftmax,height,rightmax):
            if l>=0 and r>=0:
                sum_height += max(0,min(l,r)-h)  #要选矮的那一个和自身减，因为短板效应
        return sum_height



if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    solution = Solution()
    print(solution.trap(height))