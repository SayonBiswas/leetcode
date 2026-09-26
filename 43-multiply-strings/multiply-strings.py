class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                    "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        if num1 == "0" or num2 == "0":
            return "0"
        else:
            res = [0] * (len(num1) + len(num2))
            for i in range(len(num1) - 1, -1, -1):
                for j in range(len(num2) - 1, -1, -1):
                    total = (num_dict[num1[i]] * num_dict[num2[j]]) + res[i+j+1]
                    res[i+j+1] = total % 10
                    res[i+j] += total // 10
        ptr = 0
        for k in range(len(res)):
            if res[k] != 0:
                ptr = k
                break
        result = ""
        for ch in range(ptr, len(res)):
            result += str(res[ch])
        return result