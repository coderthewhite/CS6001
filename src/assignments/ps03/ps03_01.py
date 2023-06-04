class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''
        #for each
        for c in s:
            
            if (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9' )):
                c = c.lower()
                clean_str += c
        
        #have clean str
        left = 0
        right = len(clean_str) - 1
        while left < right:
            if clean_str[left] != clean_str[right]:
                break
            left += 1
            right -= 1

        result = not (left < right) #if left < right --> True
                              #if left < right --> False
        return result

