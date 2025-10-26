
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        inorderMap = {val : idx for idx, val in enumerate(inorder)}
        self.ptr = 0

        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.ptr]
            self.ptr += 1

            split = inorderMap[root_val]

            node = TreeNode(root_val)

            node.left = build(left, split-1)
            node.right = build(split+1, right)
            return node

        return build(0, len(inorder)-1)

            
            

        