class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or position[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps