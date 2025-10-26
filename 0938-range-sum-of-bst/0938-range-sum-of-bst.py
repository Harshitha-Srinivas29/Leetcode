# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
         return self.findSum(root, low, high)
         
    def findSum(self, root,low, high):
        if not root:
            return 0
        if (low <= root.val <= high):
            sum = root.val
        else: sum = 0
        return sum + self.findSum(root.left, low, high) + self.findSum(root.right, low, high)
        
        