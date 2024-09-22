class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        check = []
        for c in s:
            if c =="I":
                res += 1
                check.append(c)
            elif c == "V":
                if "I" in check:
                    res += 3
                else:
                    res += 5
            elif c == "X":
                if "I" in check:
                    res += 8
                else:
                    res += 10
                    check.append(c)
            elif c == "L":
                if "X" in check:
                    res += 30
                else:
                    res += 50
            elif c == "C":
                if "X" in check:
                    res += 80
                else:
                    res += 100
                    check.append(c)
            elif c == "D":
                if "C" in check:
                    res += 300
                else:
                    res += 500
            elif c == "M":
                if "C" in check:
                    res += 800
                else:
                    res += 1000
        return res
