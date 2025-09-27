class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            # avoid duplicates
            elif i > 0 and nums[i] == nums[i-1]: continue

            left, right = i+1, n-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left, right = left+1, right-1
                    # avoid duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1

        return result
                    
        