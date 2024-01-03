function isValidSudoku(board: string[][]): boolean {
    const ROWS = board.length;
    const COLS = board[0].length;
    
    interface StringSetObject {
        [key: string]: Set<string>;
    }
    
    const rows: StringSetObject = {};
    const cols: StringSetObject = {};
    const squares: StringSetObject = {};
    
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            const value: string = board[row][col];
            if (value === ".") continue;
            
            if (!(row in rows)) {
                rows[row] = new Set();
            } 
            if (rows[row].has(value)) {
                return false
            };
            rows[row].add(value);
            
            if (!(col in cols)) {
                cols[col] = new Set();
            }
            if (cols[col].has(value)) return false;
            cols[col].add(value);
            
            const squareX = Math.floor(row / 3);
            const squareY = Math.floor(col / 3);
            const squareCoord = `${squareX},${squareY}`;
            
            if (!(squareCoord in squares)) {
                squares[squareCoord] = new Set();
            }
            if (squares[squareCoord].has(value)) return false;
            squares[squareCoord].add(value);
        }
    }
    
    return true;
    
};