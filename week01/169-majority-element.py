"""
Time complexity: O(n)
Memory complexity: O(1)
Idea: we can do this using hash map then memory complexity becase O(1).
So we can use Boyer–Moore majority vote algorithm to find the major element.
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # hash_map = {}
        # major_check = len(nums)/2
        # for ind, val in enumerate(nums):
        #     count = hash_map.get(val, 0) + 1
        #     hash_map[val] = count
        #     if count > major_check:
        #         return val

        majority_element = nums[0]
        count = 0
        for ind, val in enumerate(nums):
            if count == 0:
                majority_element = val
                count = 1
            elif val == majority_element:
                count += 1
            else:
                count -= 1
        return majority_element
