class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_string = s.split()
        return len(list_of_string[-1])