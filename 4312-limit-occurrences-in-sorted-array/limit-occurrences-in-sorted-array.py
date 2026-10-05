from typing import List

class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        w = 0
        for x in nums:
            if w < k or x != nums[w - k]:
                nums[w] = x
                w += 1
        return nums[:w]