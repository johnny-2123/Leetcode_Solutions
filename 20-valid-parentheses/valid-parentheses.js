/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  const openingBrackets = new Set(["(", "[", "{"]);
  const correspondingClosingBracket = {
    "(": ")",
    "{": "}",
    "[": "]"
  };

  const closingBracketStack = [];

  for (let i = 0; i < s.length; i++) {
    const currBracket = s[i];

    if (openingBrackets.has(currBracket)) {
      const closingBracket = correspondingClosingBracket[currBracket];
      closingBracketStack.unshift(closingBracket);
    } else {
      if (currBracket !== closingBracketStack[0]) {
        return false;
      } else {
        closingBracketStack.shift();
      }
    }
  }

  return closingBracketStack.length === 0;
};
