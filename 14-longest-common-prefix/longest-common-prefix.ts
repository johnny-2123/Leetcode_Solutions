function longestCommonPrefix(strs: string[]): string {
    if (!strs[0]) return "";

    let prefix: string = strs[0];

    for (const str of strs) {
        let newPrefix = "";
        let idx = 0;
        while (idx < str.length && idx < prefix.length && str[idx] === prefix[idx]) {
            newPrefix += str[idx];
            idx++;
        }
        
        prefix = newPrefix
    }

    return prefix;
};