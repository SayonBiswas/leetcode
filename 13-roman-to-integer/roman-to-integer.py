class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        res = 0
        for ch in range(len(s)):
            if ch + 1 < len(s) and roman_to_integer[s[ch]] < roman_to_integer[s[ch+1]]:
                res -= int(roman_to_integer[s[ch]])
            else:
                res += int(roman_to_integer[s[ch]])
        return res