class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tracker = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)

            if key in tracker:
                # print(key, tracker[key])
                tracker[key].append(s)
            else:
                tracker[key] = [s]
        
        for v in tracker.values():
            res.append(v)
        
        return res