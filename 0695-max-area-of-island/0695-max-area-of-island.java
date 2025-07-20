class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxCount = 0, count = 0;
        int row = grid.length, col = grid[0].length;
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(grid[i][j] == 1)
                    count = dfs(grid, i, j);
                maxCount = Math.max(count, maxCount);
            }
        }
        return maxCount;
    }

    public int dfs(int[][] grid, int i, int j){
        int count = 0;
        if(i < 0 || j < 0 || i >=  grid.length || j >=  grid[0].length || grid[i][j] == 0) return count;

        if(grid[i][j] == 1)
        count++;
        grid[i][j] = 0;

        int up = dfs(grid,i+1, j);
        int down = dfs(grid, i-1, j);
        int right = dfs(grid, i, j+1);
        int left = dfs(grid, i, j-1);
        return count + left + right + up + down;       
    }
}