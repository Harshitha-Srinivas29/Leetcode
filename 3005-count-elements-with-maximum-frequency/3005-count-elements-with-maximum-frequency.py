class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = {}
        max_freq = 0
        count = 0

        for num in nums:
            map[num] = map.get(num, 0)+1
            freq = map[num]

            if freq > max_freq:
                max_freq = freq
                count = freq
            elif freq == max_freq:
                count += freq
        return count
        

        