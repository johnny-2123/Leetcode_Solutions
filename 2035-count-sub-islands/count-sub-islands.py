class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c, grid, island: Set) -> None:
            if (r < 0 or r >= rows) or (c < 0 or c >= cols):
                return
            if grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            island.add((r, c))
            dfs(r + 1, c, grid, island)
            dfs(r - 1, c, grid, island)
            dfs(r, c + 1, grid, island)
            dfs(r, c - 1, grid, island)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid2[r][c] == 1:
                    island = set()
                    dfs(r, c, grid2, island)
                    if all(grid1[row][col] == 1 for row, col in island):
                        count += 1

        return count
