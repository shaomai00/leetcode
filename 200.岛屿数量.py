# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

from typing import List
class Solution:
    # DFS 访问相邻结点,判断badcase退出
    # 但网格结构的 DFS 与二叉树的 DFS 最大的不同之处在于，遍历中可能遇到遍历过的结点，为此，可以把已经走过的陆地格子变成2
    def inAera(self, grid, c, r):
        if 0<=c<len(grid) and 0<=r<len(grid[0]):
            return True
        return False
    def dfs(self, grid, c, r):
        if not self.inAera(grid, c, r):
            return
        if grid[c][r] != "1":  # 2代表遍历过
            return
        grid[c][r] = "2"
        self.dfs(grid, c-1,r)
        self.dfs(grid, c + 1, r)
        self.dfs(grid, c, r-1)
        self.dfs(grid, c, r+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        for c in range(len(grid)):
            for r in range(len(grid[0])):
                if grid[c][r] == "1":
                    self.dfs(grid, c, r)
                    res += 1
        return res
if __name__ == '__main__':
    solution = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(solution.numIslands(grid))