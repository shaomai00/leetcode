/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution{
    public int maxDepth(TreeNode root) {
        if(root!=null){
           int left = maxDepth(root.left);
           int right = maxDepth(root.right);
           return Math.max(left, right) + 1;
        }else{
            return 0;
        }
    }
}