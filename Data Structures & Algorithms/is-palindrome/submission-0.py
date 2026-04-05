class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_text = "".join(char for char in s if char.isalnum())

        r = clean_text.lower()

    
        if r[::-1] == r:
            return True
        return False

        