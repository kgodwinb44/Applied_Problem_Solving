# Excel Sheet Column Number

class Solution(object):
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for char in columnTitle:
            col_num = col_num * 26 + (ord(char) - 64)
        return col_num
    

sol = Solution()
print(sol.titleToNumber('BB'))
    
        