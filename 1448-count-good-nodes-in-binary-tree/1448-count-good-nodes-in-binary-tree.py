# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, float("-inf"))
        return self.count

    def dfs(self, root, currMax):
        if root.val >= currMax:
            self.count += 1
            currMax = root.val
        if root.left:
            self.dfs(root.left, currMax)
        if root.right:
            self.dfs(root.right, currMax)
        
        