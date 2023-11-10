/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    let sum = 0;
    let prevValue = 0;

    for (let i = 0; i < s.length; i ++) {
        currValue = values[s[i]];
        if (currValue > prevValue) {
            sum -= prevValue;
            sum += (currValue - prevValue);
        } else {
            sum += currValue;
        };

        prevValue = currValue;
    };

    return sum
};