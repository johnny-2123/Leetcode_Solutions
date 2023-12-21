function reverseWords(s: string): string {
    s = s.trim();
    s = s.replace(/\s+/g, ' ');
    
    const splitWords: string[] = s.split(" ");
    
    let res: string = "";
    for (const word of splitWords) {
        res = word + " " + res;
    }

    return res.trim();
};