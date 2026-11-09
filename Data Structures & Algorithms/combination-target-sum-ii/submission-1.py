class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # sort -> nlog(n)
        sortedCan = sorted(candidates)
        def dfs(i, combo):
            if i > len(sortedCan) - 1:
                return

            preCombo = list(combo)
            combo.append(sortedCan[i])

            total = 0
            for c in combo:
                total += c

            if total == target:
                res.append(combo)
            elif total < target:
                dfs(i + 1, combo)

            while i+1 <= len(sortedCan) -1 and sortedCan[i] == sortedCan[i+1]:
                    i += 1
            dfs(i + 1, preCombo)
            
        dfs(0, [])
        return res