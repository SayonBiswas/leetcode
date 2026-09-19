class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            nums1[:] = nums1[:m]
            nums1.extend(nums2)
            nums1.sort()