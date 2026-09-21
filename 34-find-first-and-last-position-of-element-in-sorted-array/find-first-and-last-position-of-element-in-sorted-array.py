class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = last = -1
        if nums == []:
            return [first, last]
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if first == -1:
                return [-1, -1]
            
            left, right, last = 0, len(nums) - 1, first
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return [first, last]