class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(i, combo):
            if i > len(nums) - 1:
                return
            
            newCombo = list(combo)
            newCombo.append(nums[i])
            # print(combo)

            sums = 0
            for c in newCombo:
                sums += c
            
            # print(sums, target)
            if sums < target:
                # print('dfs')
                dfs(i, newCombo)
                
            elif sums == target:
                self.res.append(newCombo)
            
            dfs(i+1, combo)
            return

        dfs(0, [])
        return self.res

