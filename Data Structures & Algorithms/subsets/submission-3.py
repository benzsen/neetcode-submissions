class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(sub, i):
            if i > len(nums) - 1:
                res.append(sub)
                return
            
            addSub = list(sub)
            addSub.append(nums[i])

            noAddSub = list(sub)

            dfs(addSub, i + 1)
            dfs(noAddSub, i + 1)
            # print(res)

        dfs([], 0)
        return res