class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        stack = []
        for n in digits:
            num *= 10
            num += n
        num += 1
        stack = [int(i) for i in str(num)]
        return stack