function longestPalindrome(s: string): string {
    let res: string = "";
    let maxLength: number = 0;

    for (let i = 0; i < s.length; i++) {
        let left: number = i;
        let right: number = i;
        while (left >= 0 && right < s.length && (s[left] === s[right])) {
            const currLength: number = right - left + 1;
            if (currLength > maxLength) {
                res = s.slice(left, right + 1);
                maxLength = currLength;
            }

            left--;
            right++;
        }

        left = i;
        right = i + 1;
        while (left >= 0 && right < s.length && (s[left] === s[right])) {
            const currLength: number = right - left + 1;
            if (currLength > maxLength) {
                res = s.slice(left, right + 1);
                maxLength = currLength;
            }

            left--;
            right++;
        }
    }

    return res;
};