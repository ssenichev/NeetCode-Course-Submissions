class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        word3 = ""

        while l < len(word1) and r < len(word2):
            word3 += word1[l]
            l += 1

            word3 += word2[r]
            r += 1
        
        word3 = word3 + word1[l:] + word2[r:]
        return word3