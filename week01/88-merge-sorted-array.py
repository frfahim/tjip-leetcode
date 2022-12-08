"""
Time complexity: O(n)
Memory complexity: O(1)
Topic: Two pointer
Idea: We can start comparing from 1st element and add to a new array, then MC will be O(n)
As both array's are sorted, so instead of comparing from 1st element
we can compare from last element and append in the last index of nums1.
Also we have to increase/decrease one pointer.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last_ind = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[last_ind] = nums2[n-1]
                n -= 1
            else:
                nums1[last_ind] = nums1[m-1]
                m -= 1
            last_ind -= 1
        while n > 0:
            nums1[last_ind] = nums2[n-1]
            n -= 1
            last_ind -= 1
