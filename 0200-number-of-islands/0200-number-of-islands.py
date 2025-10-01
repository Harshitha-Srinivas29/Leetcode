class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        row = len(grid)
        col = len(grid[0])

        if not grid:
            return 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    island_count += 1
        return island_count

    def dfs(self, grid, r, c) -> None:
        if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1"):
            return

        grid[r][c] = "0"

        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1) 

        