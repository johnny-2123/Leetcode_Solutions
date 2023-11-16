/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const matchingCloseParentheses = {
        "{": "}",
        "[": "]",
        "(": ")"
    };

    const stack = [];

    for (const char of s) {
        if (char in matchingCloseParentheses) {
            stack.push(char)
        } else {
            if (!(stack.length > 0)) return false
            const openP = stack.pop();
            if (char !== matchingCloseParentheses[openP]) {
                return false
            }
        }
    }
    return stack.length === 0
};