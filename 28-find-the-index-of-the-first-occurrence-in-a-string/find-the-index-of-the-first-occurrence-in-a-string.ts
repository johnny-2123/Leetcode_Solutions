function strStr(haystack: string, needle: string): number {
    if (haystack === needle) return 0;

    let left = 0;
    let right = needle.length;

    while (right <= haystack.length) {
        if (haystack.slice(left, right) === needle) {
            return left
        } else {
            left++;
            right++;
        }
    }

    return -1
};