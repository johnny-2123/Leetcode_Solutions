/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    const pairs = [];
    for (let i = 0; i < position.length; i++) {
        const [p, s] = [position[i], speed[i]]
        console.log(p, s)
        pairs.push([p, s])
    }
    console.log("pairs", pairs)

    pairs.sort((a, b) => {
        return b[0] - a[0]
    })
    console.log("pairs", pairs)

    const stack = []
    for(let i = 0; i < pairs.length; i++) {
        const [p, s] = [pairs[i][0], pairs[i][1]]
        const timeToTarget = (target - p) / s
        stack.push(timeToTarget)
        if(stack[stack.length - 1] <= stack[stack.length - 2]) stack.pop()
    }

    return stack.length
};