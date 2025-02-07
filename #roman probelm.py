#roman numerial conversion

class Solution:  
 
 def RomanToInt(self, s) -> int:
    result = 0
    symbols = {'I': 1, 'V': 5, 'X': 10}    
    
    for i in range (len(s)):
        if i + 1< len(s) and symbols[s[i]] < symbols[s[i]]:
          result -= symbols[s[i]]
        else:
            result += symbols[s[i]]
    return result

sol = Solution()
print(sol.RomanToInt('III'))
        
           