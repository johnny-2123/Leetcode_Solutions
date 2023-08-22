/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  if(s.length <= 1) {
    return false
  } 
  const openingBrackets = new Set(["(", "[", "{"]);
  const correspondingClosingBracket = {
    "(": ")",
    "{": "}",
    "[": "]"
};

  const closingBracketStack = [];

  for (let i = 0; i < s.length; i++) {
    const currBracket = s[i];
    console.log("currBracket", currBracket)
    if(openingBrackets.has(currBracket)) {
      const closingBracket = correspondingClosingBracket[currBracket];
      console.log("closingBracket", closingBracket)
      closingBracketStack.unshift(closingBracket)
      console.log("closingBracketStack", closingBracketStack)
    } else {
      if (currBracket !== closingBracketStack[0]) {
        console.log("closingBracketStack", closingBracketStack)
        return false;
      } else {
        closingBracketStack.shift();
      }
    }
  }
    return closingBracketStack.length === 0;
};