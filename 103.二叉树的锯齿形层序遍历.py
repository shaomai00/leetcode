# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# Definition for a binary tree node.
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        reverse = False
        while queue:
            size = len(queue)
            level_res = []
            for i in range(size):
                node = queue.pop()
                level_res.append(node.val)
                if node.left:
                    queue = [node.left] + queue
                if node.right:
                    queue = [node.right] + queue
            if reverse:
                res.append(level_res[::-1])
            else:
                res.append(level_res)
            reverse = not reverse

        return res
if __name__ == '__main__':
    tree = [1,2,3,4,None,None,5]
    tree = Tree(tree)
    print(tree)
    solution = Solution()
    print(solution.zigzagLevelOrder(tree.root))


