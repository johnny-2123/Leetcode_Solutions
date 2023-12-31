function spiralOrder(matrix) {
    if (!matrix || !matrix[0]) return [];
    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;
    
    let res = [];

    while (left <= right && top <= bottom) {
        for (let c = left; c <= right; c++) {
            res.push(matrix[top][c]);
        }
        top++;

        for (let r = top; r <= bottom; r++) {
            res.push(matrix[r][right]);
        }
        right--;

        if (top <= bottom) {
            for (let c = right; c >= left; c--) {
                res.push(matrix[bottom][c]);
            }
            bottom--;
        }

        if (left <= right) {
            for (let r = bottom; r >= top; r--) {
                res.push(matrix[r][left]);
            }
            left++;
        }
    }

    return res;
}
