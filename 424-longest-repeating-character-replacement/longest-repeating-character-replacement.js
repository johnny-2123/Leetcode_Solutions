/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */


var characterReplacement = function(s, k) {
    const charCounter = {};
    let longestStrLength = -Infinity;


    let [left, right] = [0, 0]
    charCounter[s[left]] = 1;
    while(right < s.length) {
        const windowLength = (right - left) + 1;
        const maxCount = Math.max(...Object.values(charCounter))
        const maxChanges = windowLength - maxCount;


        if (maxChanges <= k) {
            longestStrLength = Math.max(longestStrLength, windowLength);
            right++;
            charCounter[s[right]] = (charCounter[s[right]] || 0) + 1;
        } else {
            charCounter[s[left]] -= 1;
            left++;
        }
    }


    return Math.max(longestStrLength || 0)
};