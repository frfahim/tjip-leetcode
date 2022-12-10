class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # seen_nums = set()
        # for val in nums:
        #     if val in seen_nums:
        #         seen_nums.remove(val)
        #     else:
        #         seen_nums.add(val)
        # return seen_nums.pop()

        ans = 0
        for val in nums:
            ans ^= val
        return ans
