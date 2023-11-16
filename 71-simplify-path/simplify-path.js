/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    const splitPath = path.split("/");
    console.log("splitPath", splitPath);

    const simplifiedPath = []
    for (let el of splitPath) {
        if (el && !(el == ".") & !(el == "..")) {
            simplifiedPath.push(el)
        }
        if (el == "..") {
            simplifiedPath.pop()
        }
    }
    return `/${simplifiedPath.join("/")}`
};