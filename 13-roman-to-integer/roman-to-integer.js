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
        for (let i = 0; i < s.length; i++) {
            if (s[i] === "I") {
                sum += values["I"]
            } else if (s[i] === "V") {
                if (i > 0 && s[i - 1] === "I"){
                    sum -= values["I"];
                    sum += 4
                } else {
                    sum += values["V"]
                }
            } else if (s[i] === "X") {
                if (i > 0 && s[i - 1] === "I") {
                    sum -= values["I"];
                    sum += 9
                } else {
                    sum += values["X"]
                }
            } else if (s[i] === "L"){
                if (i > 0 && s[i - 1] === "X") {
                    sum -= values["X"];
                    sum += 40
                } else {
                    sum += values["L"]
                }
            } else if (s[i] === "C") {
                if (i > 0 && s[i - 1] === "X") {
                    sum -= values["X"];
                    sum += 90
                } else {
                    sum += values["C"]
                }
            } else if (s[i] === "D") {
                if (i > 0 && s[i - 1] === "C") {
                    sum -= values["C"];
                    sum += 400;
                } else {
                    sum += values["D"]
                }
            }  else if (s[i] === "M") {
                if (i > 0 && s[i - 1] === "C") {
                    sum -= values["C"];
                    sum += 900
                } else {
                    sum += values["M"]
                }
            }
        }

        return sum
};