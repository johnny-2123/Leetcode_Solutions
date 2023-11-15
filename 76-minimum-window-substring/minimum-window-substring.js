/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
  if (t === "") return "";

  let countT = {};
  let window = {};

  for (let i = 0; i < t.length; i++){
      const char = t[i];
      if (char in countT) {
          countT[char]++; 
      } else {
          countT[char] = 1
      }
  }

  let have = 0;
  const need = Object.keys(countT).length; 

  let res = "";
  let resLength = Infinity; 

  let left = 0;

  for (let right = 0; right < s.length; right++){
      char = s[right];
      if(char in window) {
          window[char]++;
      } else {
          window[char] = 1;
      }

      if (countT[char] && (window[char] == countT[char])) {
          have += 1;
      }

      while (have >= need) {
          if ((right - left + 1) < resLength) {
              res = s.slice(left, right + 1);
              resLength = (right - left + 1)
          }

          const leftChar = s[left];
          window[leftChar] -= 1; 

          if(leftChar in countT && (window[leftChar] < countT[leftChar])) {
              have -= 1;
          }
          
          left += 1;
      } 
  }
  
    return res

};
