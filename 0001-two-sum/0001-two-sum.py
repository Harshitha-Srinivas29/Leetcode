class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem not in map:
                map[nums[i]] = i
            else:
                return [i, map[rem]]
        return []