/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const trimmedString = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let [leftIdx, rightIdx] = [0, trimmedString.length - 1];


    while (leftIdx < trimmedString.length - 1) {
        const leftChar = trimmedString[leftIdx];
        const rightChar = trimmedString[rightIdx];


        if(leftChar !== rightChar){
            return false
        }


        leftIdx += 1;
        rightIdx -= 1;
    }


    return true
};
