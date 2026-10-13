class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length