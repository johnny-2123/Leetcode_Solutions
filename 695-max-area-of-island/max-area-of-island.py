class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        currArea = 0

        def _inBound(row, col):
            
            rowInBound = 0 <= row and row < len(grid)
            colInBound = 0 <= col and col < len(grid[0])

            return rowInBound and colInBound

        def _dfs(row, col):
            nonlocal currArea

            if not _inBound(row, col):
                return

            if grid[row][col] == 0:
                return
            
            pos = f'{row},{col}'
            if pos in visited:
                return
        
            visited.add(pos)

            _dfs(row + 1, col)
            _dfs(row - 1, col)
            _dfs(row, col + 1)
            _dfs(row, col - 1)
            
            if grid[row][col] == 1:
                currArea += 1

        visited = set()

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                _dfs(row, col)
                maxArea = max(maxArea, currArea)
                currArea = 0
        
        return maxArea

