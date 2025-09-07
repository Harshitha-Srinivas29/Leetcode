class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        i = 0
        j = 1
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j] , nums[i]
                i += 1
            

        
        