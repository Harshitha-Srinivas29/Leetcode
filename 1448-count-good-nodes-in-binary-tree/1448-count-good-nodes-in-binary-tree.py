# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, curr_max):
            nonlocal count
            if curr_max <= root.val:
                count += 1
                curr_max = root.val
            if root.left:
                dfs(root.left, curr_max)
            if root.right:
                dfs(root.right, curr_max)

        dfs(root, float("-inf"))
        return count
        