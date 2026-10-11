
class Solution:
    def maximumMedianSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)

        total = 0
        n = len(nums)

        for i in range(1, n * 2 // 3, 2):
            total += nums[i]

        return total

        