# LCA  给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 最近公共祖先可以用于解决很多关于二叉树的问题，例如：
#
# 查找两个节点的距离
# 查找从一个节点到另一个节点的路径
# 查找两个节点在树中的相对位置关系（例如，是否是祖先/后代关系）

from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self, nums: List):
        self.root = TreeNode(val = nums[0])
        new_list = [self.root]
        for i in range(1,len(nums),2):
            left_node = TreeNode(val = nums[i]) if nums[i]!=None else None
            right_node = TreeNode(val = nums[i+1]) if nums[i+1]!=None else None
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
            if node.left!=None:
                queue = [node.left] + queue
            if node.right!=None:
                queue = [node.right] + queue
        return str(res)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归法求解
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # p,q都找到了分别在左右
            return root
        if left and not right:  return left # 在右边继续找
        if right and not left: return right   # 在左边继续找
        return None   # 都没找到返回空

if __name__ == '__main__':
    solution = Solution()
    # tree = [3, 9, 20, None, None, 15, 7]
    tree = [3,5,1,6,2,0,8,None,None,7,4]
    tree = Tree(tree)
    print(tree)
    # [[3],[9,20],[15,7]]
    print(solution.lowestCommonAncestor(tree.root,5,1))