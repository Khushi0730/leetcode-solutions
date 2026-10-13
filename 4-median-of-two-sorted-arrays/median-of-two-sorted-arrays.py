class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            aL = A[i - 1] if i > 0 else float('-inf')
            aR = A[i] if i < m else float('inf')
            bL = B[j - 1] if j > 0 else float('-inf')
            bR = B[j] if j < n else float('inf')

            if aL <= bR and bL <= aR:
                if (m + n) % 2:
                    return max(aL, bL)
                return (max(aL, bL) + min(aR, bR)) / 2
            elif aL > bR:
                hi = i - 1
            else:
                lo = i + 1