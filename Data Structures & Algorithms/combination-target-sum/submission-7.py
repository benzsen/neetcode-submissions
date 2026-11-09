class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(combo, i):
            if i > len(nums) - 1:
                return
            preCombo = list(combo)

            combo.append(nums[i])

            total = 0
            for c in combo:
                total += c
            dfs(preCombo, i+1)

            # print(combo, total, target)
            if total < target:
                dfs(combo, i)
            elif total == target:
                res.append(combo)
            
            return

        dfs([], 0)
        return res
