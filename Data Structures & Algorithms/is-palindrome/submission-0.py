class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        text = "".join(filter(str.isalnum, s)).lower()
        
        low = 0
        high = len(text)-1

        while low<=high :
            if text[low] != text[high] :
                return False

            else :
                low+=1
                high-=1

        return True

        