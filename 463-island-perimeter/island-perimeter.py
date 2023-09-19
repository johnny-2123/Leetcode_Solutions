class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island = set()

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    island.add(f"{row},{col}")
        
        perimeter = 0

        for coordinate in island:
            parts = coordinate.split(",")
            row = int(parts[0])
            col = int(parts[1])
            
            openSides = 4

            top = f"{row - 1},{col}"
            if top in island:
                openSides -= 1
            bot = f"{row + 1},{col}"
            if bot in island:
                openSides -= 1
            right = f"{row},{col + 1}"
            if right in island:
                openSides -= 1
            left = f"{row},{col - 1}"
            if left in island:
                openSides -= 1
            perimeter += openSides

        return perimeter