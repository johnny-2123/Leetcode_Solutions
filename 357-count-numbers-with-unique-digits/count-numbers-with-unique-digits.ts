function countNumbersWithUniqueDigits(n: number): number {
    if (n === 0) return 1;

    let res: number = 10;
    let start: number = 9;
    let curr: number = 9;

    while (n > 1 && start) {
        curr *= start;
        start--;

        res += curr;
        n--
    }

    return res;
};