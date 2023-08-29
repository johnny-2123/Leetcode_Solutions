/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let [left, right] = [0, 0];
    let maxLength = 0;
    const window = new Set();

    while (right < s.length) {
        const rightChar = s[right];

        if (window.has(rightChar)) {
            while (s[left] !== rightChar) {
                window.delete(s[left]);
                left += 1;
            }
            left += 1; 
        }

        window.add(rightChar);
        maxLength = Math.max(maxLength, window.size);
        right += 1;
    }

    return maxLength;
};
