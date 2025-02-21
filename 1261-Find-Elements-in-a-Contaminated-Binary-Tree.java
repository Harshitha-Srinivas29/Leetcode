/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class FindElements {
    HashSet<Integer> visited;

    public FindElements(TreeNode root) {
        visited = new HashSet<>();
        dfs(root,0);
    }
    
    public boolean find(int target) {
        return visited.contains(target);
    }

    public void dfs(TreeNode curr, int currVal){
        if(curr == null) return;

        visited.add(currVal);
        
        dfs(curr.left, currVal*2+1);
        dfs(curr.right, currVal*2+2);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */