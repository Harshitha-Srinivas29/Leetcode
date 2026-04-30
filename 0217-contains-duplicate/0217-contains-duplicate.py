class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_list = set()

        for num in nums:
            num_list.add(num)

        if len(nums) == len(num_list):
            return False
        return True
        
    

        