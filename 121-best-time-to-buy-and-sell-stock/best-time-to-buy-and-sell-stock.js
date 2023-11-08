/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let left = 0;
    let maxProfit = 0;

    prices.forEach((rightPrice, right) => {
        const leftPrice = prices[left];
        const currProfit = rightPrice - leftPrice;
        maxProfit = Math.max(currProfit, maxProfit);

        if (leftPrice > rightPrice) {
            left = right
        }
    });

    return maxProfit;
};