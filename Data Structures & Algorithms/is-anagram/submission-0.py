class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = dict()
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        for char in t:
            chars[char] = chars.get(char, 0) - 1
        for n in chars.values():
            if n != 0:
                return False
        return True

