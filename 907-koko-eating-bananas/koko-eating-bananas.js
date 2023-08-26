/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let left = 0;
    let right = Math.max(...piles);
    let minK = right;

    while (left <=right) {
        let k = Math.floor((right + left) / 2);
        console.log("k", k)
        let totalHours = 0;

        for(let i = 0; i < piles.length; i++) {
            let hoursForPile = Math.ceil(piles[i] / k);
            totalHours += hoursForPile;
        }
        console.log("totalHours", totalHours)
        if(totalHours <= h) {
            minK = Math.floor(k, minK);
            right = k - 1;
        } else {
            left = k + 1;
        }
    }

    return minK;
};