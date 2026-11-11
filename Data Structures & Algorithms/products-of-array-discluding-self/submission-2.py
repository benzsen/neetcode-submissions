class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[0] = 1
            else:
                pre[i] = pre[i-1] * nums[i-1]
                

        post = [0] * len(nums)
        for j in range(len(nums)-1, -1, -1):

            if j == len(nums)-1:
                post[j] = 1
            else:
                post[j] = post[j+1]*nums[j+1]

        res = [0] * len(nums)
        for x in range(len(pre)):
            res[x] = pre[x]*post[x]

        return res
