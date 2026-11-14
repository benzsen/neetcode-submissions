class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(subList):
            if not subList:
                self.res.append([])
                # print("self.res", self.res)
                return 
            
            # print(subList, self.res)
            # childList = dfs(subList[1:])
            dfs(subList[1:])

            tmp = []
            newNum = subList[0]

            print(self.res)
            for r in self.res:
                print(tmp)
                # if not r:
                #     tmp.append([newNum])
                #     self.res = tmp
                
                for i in range(len(r)+1):
                    # print(r, tmp, newNum)
                    tmpR = list(r)
                    tmpR.insert(i, newNum)
                    tmp.append(tmpR)
                    # print(r, tmp, newNum)

                    self.res = tmp

        dfs(nums)
        return self.res