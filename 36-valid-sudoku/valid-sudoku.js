/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const rows = {};
    const cols = {};
    const squares = {};

   for(let r = 0; r < board.length; r++) {
        for (let c = 0; c < board[r].length; c++) {
            const value = board[r][c];
            if(value === '.') continue

            let rowSet = rows[r];
            if (!rowSet) {
                rowSet = new Set();
                rows[r] = rowSet;  
            }

            if (rowSet.has(value)) {
                return false;
            } else {
                rowSet.add(value);
            }

            let colSet = cols[c];
            if (!colSet) {
                colSet = new Set();
                cols[c] = colSet; 
            }

            if (colSet.has(value)) {
                return false;
            } else {
                colSet.add(value);
            }

            const squareX = Math.floor(r / 3);
            const squareY = Math.floor(c / 3);
            const squareCoordinates = `${squareX},${squareY}`;
            console.log(squareCoordinates)

            let squareSet = squares[squareCoordinates];
            if (!squareSet) {
                squareSet = new Set();
                squares[squareCoordinates] = squareSet;  
            }

            if (squareSet.has(value)) {
                return false;
            } else {
                squareSet.add(value);
            }
        }
    }

    return true;
};