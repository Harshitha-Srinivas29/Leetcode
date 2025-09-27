class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder not in map:
                map[nums[i]] = i
            else:
                return [i, map[reminder]]
        return []