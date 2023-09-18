class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _dfs(row, col):
            if not _inBound(row, col):
                return False
            
            if grid[row][col] == "0":
                return False

            pos = f'{row},{col}'
            if pos in visited:
                return False
            
            visited.add(pos)
            print("pos", pos)

            _dfs(row + 1, col)
            _dfs(row - 1, col)
            _dfs(row, col + 1)
            _dfs(row, col - 1)
            return True

        def _inBound(row, col):
            rowInBound = 0 <= row and row < len(grid)
            colInBound = 0 <= col and col < len(grid[0])
            return rowInBound and colInBound

        count = 0 
        visited = set()

        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if _dfs(r, c):
                    count += 1
        
        return count