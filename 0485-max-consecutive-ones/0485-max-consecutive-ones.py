class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        maxCount = -1

        for i in range(n):
            if nums[i] == 1:
                count = count + 1
                maxCount = max(count, maxCount)
                continue
            else:
                count = 0

        return maxCount
        