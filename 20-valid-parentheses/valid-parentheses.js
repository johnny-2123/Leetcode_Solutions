/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const bracketPairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    };

    for (let i = 0; i < s.length; i++) {
        const currChar = s[i];

        if (currChar in bracketPairs) {
            stack.push(currChar);
        } else {
            if (stack.length === 0) {
                return false; // Unmatched closing bracket
            }

            const topBracket = stack.pop();
            if (bracketPairs[topBracket] !== currChar) {
                return false; // Mismatched opening and closing brackets
            }
        }
    }

    return stack.length === 0; // Check if all brackets were matched and closed
};
