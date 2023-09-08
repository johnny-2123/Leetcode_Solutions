/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const visited = new Set()
    for (let y = 0; y < matrix.length; y++) {
        const subArray = matrix[y]

        for(let x = 0; x < subArray.length; x++) {
            if(visited.has(`${y},${x}`)) continue
            const currNum = matrix[y][x];
            if(currNum === 0){
                for (let i = 0; i < subArray.length; i++) {
                    if(matrix[y][i] !== 0){
                        matrix[y][i] = 0
                        visited.add(`${y},${i}`)
                    }
                }

                for(let k = 0; k < matrix.length; k++){
                    if(matrix[k][x] !== 0) {
                        matrix[k][x] = 0
                        visited.add(`${k},${x}`)
                    }   
                }
            }
            visited.add(`${y},${x}`)
        }

        
    }

    console.log('visited', visited)

};