class Solution:
    def longestPalindrome(self, s: str) -> str:
        x1, x2 = 0, 0

        best_x1, best_x2 = 0, 0
        best_diameter = 0

        while x2 < len(s):
            point1 = x1
            point2 = x2

            while (point2 < len(s)) and (point1>-1) and (s[point1] == s[point2]):
                point1 -= 1
                point2 += 1
            point1 += 1
            point2 -= 1

            if (point2-point1) > best_diameter:
                best_x1 = point1
                best_x2 = point2
                best_diameter = point2-point1

            #end cases
            if (x1 == x2):
                x2 += 1
            else:
                x1 += 1
        
        return s[best_x1:(best_x2+1)]
    