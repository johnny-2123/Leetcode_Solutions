class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i): 
            total  = sum(subset)
            if total == target:
                ans.append(subset.copy())
                return

            if total > target or i == len(candidates):
                return 

            subset.append(candidates[i])
            dfs(i)
            
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return ans