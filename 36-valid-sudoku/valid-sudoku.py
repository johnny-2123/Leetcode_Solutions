import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue    
                
                rowSet = rows.get(r)
                if not rowSet:
                    rowSet = set()
                    rows[r] = rowSet
                
                if val in rowSet:
                    return False
                else:
                    rowSet.add(val)

                colSet = cols.get(c)
                if not colSet:
                     colSet = set()
                     cols[c] = colSet

                if val in colSet:
                    return False
                else:
                    colSet.add(val)
                
                squareX = r // 3
                squareY = c // 3
                squareCoordinates = f"{squareX},{squareY}"

                squareSet = squares.get(squareCoordinates)
                if not squareSet:
                    squareSet = set()
                    squares[squareCoordinates] = squareSet
                
                if val in squareSet:
                    return False
                else:
                    squareSet.add(val)

        return True
                    
                    
                    
        
