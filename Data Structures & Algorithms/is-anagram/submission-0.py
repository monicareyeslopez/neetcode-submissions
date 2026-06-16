class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_text = "".join(sorted(s))
        sorted_text2 = "".join(sorted(t))
        if sorted_text == sorted_text2:
            return True
        return False