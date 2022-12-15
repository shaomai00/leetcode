# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, nums: List):
        self.root = TreeNode(val = nums[0])
        new_list = [self.root]
        for i in range(1,len(nums),2):
            left_node = TreeNode(val = nums[i]) if nums[i] else None
            right_node = TreeNode(val = nums[i+1]) if nums[i+1] else None
            node = new_list.pop()
            node.left = left_node
            node.right = right_node
            new_list = [right_node, left_node] + new_list
    def __repr__(self):
        queue = [self.root]
        res = []
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.left:
                queue = [node.left] + queue
            if node.right:
                queue = [node.right] + queue
        return str(res)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            level_res = []
            for _ in range(size):  # size代表这层有几个元素
                node = queue.pop()
                level_res.append(node.val)
                if node.left:
                    queue = [node.left] + queue
                if node.right:
                    queue = [node.right] + queue
            res.append(level_res)
        return res

if __name__ == '__main__':
    solution = Solution()
    # tree = [3, 9, 20, None, None, 15, 7]
    tree = [1,2,3,4,5]
    tree = Tree(tree)
    # [[3],[9,20],[15,7]]
    print(solution.levelOrder(tree.root))
