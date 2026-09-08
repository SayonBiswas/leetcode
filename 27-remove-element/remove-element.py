class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = nums.copy()
        for fast in slow:
            if fast == val:
                nums.remove(fast)
        return len(nums)