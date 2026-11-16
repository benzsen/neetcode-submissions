class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(numbers):
            if not numbers:
                self.res.append([])
                return 

            subNums = list(numbers[1:])
            perms = dfs(subNums)
            # print(subNums, self.res)

            newLetter = numbers[0]
            tmp = []

            for r in self.res:
                # print('r', r, len(r)+1)

                for i in range(len(r)+1):
                    rCopy = list(r)
                    rCopy.insert(i, newLetter)
                    tmp.append(rCopy)
                    # print('tmp', tmp)
            self.res = tmp

        dfs(nums)
        return self.res

            