class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashmap:
                return [i, hashmap[remainder]]
            hashmap[nums[i]] = i
        return []


