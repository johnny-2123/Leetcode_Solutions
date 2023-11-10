/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let lastLength = 0;
    let currLength = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] !== " ") {
          currLength++;
          lastLength = currLength;
        } else {
          currLength = 0
        }
    }

    return lastLength
};