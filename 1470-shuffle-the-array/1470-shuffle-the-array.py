class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        j = 0

        for j in range(n):
            ans.append(nums[j])
            ans.append(nums[j+n])

        return ans

        