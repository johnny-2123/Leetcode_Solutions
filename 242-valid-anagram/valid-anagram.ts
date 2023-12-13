function isAnagram(s: string, t: string): boolean {
    const sortedS: string = s.split("").sort().join("");
    const sortedT: string = t.split("").sort().join("");

    return sortedS === sortedT;
    
};