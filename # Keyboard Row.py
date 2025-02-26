# Keyboard Row

class Solution(object):
    def findWords(self, words):
    
      a = set("qwertyuiop")
      b = set("asdfghjkl")
      c = set("zxcvbnm")
     
      result = []
     
      for word in words:           
        lowcase_word = set(word.lower())        
        if lowcase_word <= a or lowcase_word <= b or lowcase_word <= c:
            result.append(word)            
      return result

words = ["Hello","Alaska","Dad","Peace"]    
sol = Solution()
print(sol.findWords(words))

