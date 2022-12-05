class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_data = {}
        for ind, val in enumerate(nums):
            cur_value = target - val
            if cur_value in seen_data:
                return [seen_data[cur_value], ind]
            seen_data[val] = ind
