/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let left = 0;
    let maxProfit = 0;

    for (let right = 0; right < prices.length; right++) {
        const leftPrice = prices[left];
        const rightPrice = prices[right];
        const currProfit = rightPrice - leftPrice;
        maxProfit = Math.max(currProfit, maxProfit);

        if (leftPrice > rightPrice) {
            left = right
        }
    };

    return maxProfit;
};