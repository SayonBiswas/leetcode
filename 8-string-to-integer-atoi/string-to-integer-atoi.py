class Solution:
    def myAtoi(self, s: str) -> int:
        digits = "1234567890"
        s1 = ""
        s = s.strip()

        if s == "":
            return 0
        elif s[0].isalpha():
            return 0

        for ch in s:    
            if (ch == "-" or ch == "+") and s1 == "":
                s1 += ch
            elif ch in digits:
                s1 += ch
            else:
                break
        
        if s1 == "" or s1 == "-" or s1 == "+":
            return 0
        
        sign = 1
        start = 0
        if s1[0] == "-":
            sign = -1
            start = 1
        elif s1[0] == "+":
            start = 1
        result = 0
        for ch in s1[start:]:
            result = result * 10 + int(ch)
        result = sign * result

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
            
        return result