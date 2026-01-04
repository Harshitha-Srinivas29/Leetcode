class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for num in numSet:
            # Check if num is the start of the seq
            if num-1 not in numSet:
                count = 1
                curr = num
                while curr + 1 in numSet:
                    count += 1
                    curr += 1
                longestSeq = max(count, longestSeq)
        return longestSeq


# Convert List to Set:
# num_set = set(nums)
# Convert the list nums to a set num_set to allow O(1) time complexity for checking the presence of elements. This step ensures that we can quickly determine if a number is part of the sequence.

# Initialize the Longest Sequence Length:
# longest = 0
# Initialize a variable longest to keep track of the length of the longest consecutive sequence found so far. Set it to 0 initially.

# Iterate Through Each Number in the List:

# for n in nums:
# Iterate through each number n in the list nums.
# Check if Current Number is the Start of a Sequence:

# if n - 1 not in num_set:
# For each number n, check if n - 1 is not in num_set. This check determines if n is the start of a new sequence. If n - 1 is not present, it means n is the smallest number in the current sequence.