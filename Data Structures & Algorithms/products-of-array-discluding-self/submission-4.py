class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                res[0] = 1
            else:
                res[i] = res[i-1] * nums[i-1]
        
        post = 0
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                post = 1
                res[j] = res[j] * post
            else:
                post = post * nums[j+1]
                res[j] = res[j] * post

        return res
