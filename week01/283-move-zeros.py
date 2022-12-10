"""
Time complexity: O(n)
Memory complexity: O(1)
Topic: Two pointer
Idea: Problem describe we have to move zeros, but we can think oppositely.
Initially keep one pointer in 0 and traverse in array to find non zero element.
when non zero element found, swap them and increse the pointer by 1.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # point1, point2 = 0, 1
        # while point2 < len(nums):
        #     if nums[point1] == 0 and nums[point2] != 0:
        #         nums[point1], nums[point2] = nums[point2], nums[point1]
        #         point1 += 1
        #         point2 += 1
        #     elif nums[point1] == 0 and nums[point2] == 0:
        #         point2 += 1
        #     else:
        #         point1 += 1
        #         point2 += 1

        zero_point = 0
        for ind, val in enumerate(nums):
            if val != 0:
                nums[zero_point], nums[ind] = nums[ind], nums[zero_point]
                zero_point += 1
