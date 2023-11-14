/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let [tIdx, sIdx] = [0, 0];

    while (tIdx < t.length && sIdx < s.length){
        if (t[tIdx] === s[sIdx]){
            tIdx++;
            sIdx++;
        } else {
            tIdx++;
        }
    }

    return sIdx >= s.length;
};