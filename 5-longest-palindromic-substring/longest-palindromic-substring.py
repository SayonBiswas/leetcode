class Solution:
    def longestPalindrome(self, s: str) -> str:
        final_string = ""
        for ch in range(len(s)):
            left, right = ch, ch
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(final_string):
                    final_string = s[left : right+1]
                left -= 1
                right += 1
            left, right = ch, ch + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(final_string):
                    final_string = s[left : right+1]
                left -= 1
                right += 1
        return final_string