class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True
            prev_max = 0
            for s in range(0, n, k):
                block = nums[s:s + k]

                # blocks must be ordered relative to each other
                if min(block) < prev_max:
                    ok = False
                    break

                # circular descents inside the block
                desc = sum(block[i] > block[i + 1] for i in range(k - 1))
                desc += block[-1] > block[0]
                if desc > 1:
                    ok = False
                    break

                prev_max = max(block)

            if ok:
                total += k

        return total