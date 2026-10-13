class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        z = nums.count(0)
        n = len(nums)
        return nums[:n - z].count(0)