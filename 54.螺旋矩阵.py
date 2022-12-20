# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
from typing import List
import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        res = []
        while start * 2 < min(m,n):
            # 以start为起点遍历一圈
            endX = n - start
            endY = m - start
            for i in range(start, endX):
                res.append(matrix[start][i])
            if start +1 == endY: # 重要！如果已经只有横排，没有纵排，就要提前结束，不然后面向左会有问题
                break
            for j in range(start + 1, endY):
                res.append(matrix[j][endX-1])
            if start == endX -1: # 重要！如果已经只有纵排，没有横排，就要提前结束，不然后面向上会有问题
                break
            for i in range(endX -1 -1, start-1, -1):
                res.append(matrix[endY-1][i])
            for j in range(endY -1-1, start, -1):
                res.append(matrix[j][start])
            start += 1
        return res

if __name__ == '__main__':
    matrix = [[7],[9],[6]]
    solution = Solution()
    print(solution.spiralOrder(matrix))
