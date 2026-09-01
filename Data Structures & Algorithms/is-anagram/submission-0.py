class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort both strings and check for equality
        S = list(s)
        S.sort()

        T = list(t)
        T.sort()

        if S==T:
            return True
        else:
            return False