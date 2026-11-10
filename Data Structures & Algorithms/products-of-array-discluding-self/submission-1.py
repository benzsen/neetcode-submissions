class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        for i in range(len(nums)):
            if i == 0:
                pre.append(1*nums[i])
            else:
                pre.append(pre[i-1]*nums[i])

        post = [0] * len(nums)
        for j in range(len(nums)-1, -1, -1):

            if j == len(nums)-1:
                post[j] = nums[j]
            else:
                post[j] = post[j+1]*nums[j]

        res = [0] * len(nums)
        for x in range(len(pre)):
            if x == 0:
                res[x] = post[x+1]
            elif x == len(nums) -1:
                res[x] = pre[x-1]
            else:
                res[x] = pre[x-1]*post[x+1]

        return res

    