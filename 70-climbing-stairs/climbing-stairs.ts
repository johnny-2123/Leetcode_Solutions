function climbStairs(n: number): number {
    let one: number = 1;
    let two: number = 1;

    for (let i = 0; i < n - 1; i++) {
        [one, two] = [one + two, one]
    }

    return one
};