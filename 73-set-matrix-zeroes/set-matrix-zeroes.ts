/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    if (!matrix || !matrix[0]) return
    const ROWS: number = matrix.length;
    const COLS: number = matrix[0].length;

    const rowSet = new Set<number>()
    const colSet = new Set<number>()

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (matrix[r][c] == 0) {
                rowSet.add(r)
                colSet.add(c)
            }
        } 
    }

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (rowSet.has(r) || colSet.has(c)) {
                matrix[r][c] = 0
            }
        } 
    }
};