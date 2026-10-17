from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, val):
            length = right - left + 1

            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + val * val * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + val * length
            ) % MOD

            lazy[node] += val

        def push(node, left, right):
            if lazy[node] != 0 and left != right:
                mid = (left + right) // 2

                apply(node * 2, left, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, right, lazy[node])

                lazy[node] = 0

        def update(node, left, right, ql, qr, val):
            if ql <= left and right <= qr:
                apply(node, left, right, val)
                return

            push(node, left, right)

            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr, val)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr, val)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, num in enumerate(nums):
            left = last_seen.get(num, -1) + 1

            update(1, 0, n - 1, left, i, 1)

            answer = (answer + tree_sq[1]) % MOD

            last_seen[num] = i

        return answer