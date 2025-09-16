class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_count1 = -1
        max_count2 = -1
        map1 = {}
        map2 = {}
        for c in s:
            if c in 'aeiou':
                map1[c] = map1.get(c,0)+1
            else:
                map2[c] = map2.get(c,0)+1

        max_count1 = max(map1.values(), default = 0)
        max_count2 = max(map2.values(), default = 0)
            
        return max_count1 + max_count2
        

        