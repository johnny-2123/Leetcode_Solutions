function romanToInt(s: string): number {
    const values: {[key: string]: number} = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    };
    
    let total: number = 0;
    let prev: number = 0;

    for (const char of s) {
        const currValue: number = values[char];

        if (currValue > prev) {
            total -= prev;
            total += currValue - prev;
        } else {
            total += currValue
        }

        prev = currValue
    };

    return total
};