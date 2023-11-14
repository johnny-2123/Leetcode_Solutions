/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const trimmedString = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let [left, right] = [0, trimmedString.length - 1];
    while (left < trimmedString.length - 1) {
        if (trimmedString[left] !== trimmedString[right]){
            return false
        }
        left++;
        right--;
    }

    return true
};