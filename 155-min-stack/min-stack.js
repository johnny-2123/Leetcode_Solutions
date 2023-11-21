
var MinStack = function() {
    this.stack = [];
    this.minStack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push(val);
    if (this.minStack.length > 0){
        this.minStack.push(Math.min(val, this.minStack[this.minStack.length - 1]));
    } else {
        this.minStack.push(val);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if (this.stack) {
        this.stack.pop();
        this.minStack.pop();
    } 
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    if (this.stack) {
        return this.stack[this.stack.length - 1]
    } 
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    if(this.minStack) {
        return this.minStack[this.minStack.length - 1];
    } 
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */