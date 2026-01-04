class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target: 
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else: 
                left += 1

        return [-1, -1]
        