# Add Binary

class Solution(object):
    def addBinary(self, a, b):
        
        # carry variable
        carry = 0
        # pointer right to left for a
        i = len(a) -1
        # pointer right to left for b
        j = len(b) - 1
        # Not sure
        s = []
        
        while i >=0 or j>=0 or carry==1:
            if i>=0:
                carry += int (a[i])
                i -= 1
            if j>=0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry%2))
            carry //=2
        return ''.join(reversed(s))
            
            

        