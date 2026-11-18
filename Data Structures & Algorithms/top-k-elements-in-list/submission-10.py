class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = [[] for _ in range(len(nums) + 1)]
        res=[]
        count={}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        for num, c in count.items():
            tracker[c].append(num)


        # print (count)
        # print (tracker)

        while len(res) < k:
            items = tracker.pop()
            if not items:
                continue
            for i in items:
                res. append(i)
        
        return res