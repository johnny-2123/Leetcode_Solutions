/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(str1, str2) {
    return [...str1].sort().join() === [...str2].sort().join();
};