class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        # Count characters in s
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1

        # Count characters in t
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        # Compare frequency dictionaries
        return freq_s == freq_t
        
        
        