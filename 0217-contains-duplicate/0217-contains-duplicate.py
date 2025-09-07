class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for c in counts.values():
            if c > 1:
                return True
        return False
        