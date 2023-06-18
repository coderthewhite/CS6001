class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        t = abcdegh
        s = ace

        1) sl = 0
           f = 0
           t[f] == s[sl] --> sl = 1, f = 1
        2) sl = 1, f = 2
        3) sl = 2, f = 3
        4) sl = 2, f = 4
        5) sl = 3, f = 5
        6) t[f] vs s[sl]
        """
        slower = 0
        for faster in range(len(t)):
            if slower < len(s) and t[faster] == s[slower]:
                slower += 1
        
        return (slower == len(s))

