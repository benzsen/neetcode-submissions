class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        array = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        # Bucket Sort
        for num, freq in hashmap.items():
            array[freq].append(num)
        
        res = []
        for i in range(len(array)-1, 0, -1):
            for nums in array[i]:
                res.append(nums)
                if len(res) == k:
                    return res
            
        
