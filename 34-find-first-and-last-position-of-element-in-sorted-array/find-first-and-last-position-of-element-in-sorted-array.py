from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(x):
            lo, hi = 0, len(nums)  
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        first = lower_bound(target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = lower_bound(target + 1) - 1
        return [first, last]