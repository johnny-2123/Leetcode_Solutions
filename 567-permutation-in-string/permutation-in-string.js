/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    const s1Count = {}
    for (let letter of s1) {
        s1Count[letter] = 1 + (s1Count[letter] || 0);
    }
    const s1UniqueLetters = Object.keys(s1Count).length;

    const s2Count = {}
    let [left, right] = [0, s1.length - 1];
    for (let i = 0; i <= right; i++) {
        const letter = s2[i];
        s2Count[letter] = 1 + (s2Count[letter] || 0)
    }
    while(right < s2.length) {
        let matchingLettersCount = 0;
        
        for(let key in s1Count) {
            if(s1Count[key] === s2Count[key]) matchingLettersCount++;
        }
        if(matchingLettersCount === s1UniqueLetters) return true
    
        const leftLetter = s2[left]
        s2Count[leftLetter] -= 1;
        left++;

        right++;
        const rightLetter = s2[right]
        s2Count[rightLetter] = 1 + (s2Count[rightLetter] || 0)
    }

    return false
};