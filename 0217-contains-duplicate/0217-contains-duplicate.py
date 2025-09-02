class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d and d[n]>=1:
                return True
            else:
                d[n] = d.get(n, 0)+1
        
        return False