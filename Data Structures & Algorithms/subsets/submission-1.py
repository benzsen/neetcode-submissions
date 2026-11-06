class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # num is wip subset, new is new num to be added (or not)
        def dfs(sub, i):
            # print('res', res)
            # print('loop', i)
            if i > len(nums) - 1:
                res.append(sub)
                return

            subNoAdd = list(sub)
            sub.append(nums[i])

            dfs(sub, i + 1)
            dfs(subNoAdd, i + 1)
        
        # dfs([], 0, True)
        # dfs([], 0, False)
        dfs([], 0)
        return res
