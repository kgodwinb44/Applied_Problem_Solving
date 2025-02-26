# Playfair Cypher

def PlayfairCode(plainText, codePhrase):
    # Write your code here
    
    cipherText = ''
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    fixedPlainText = []
    
    # Replace Js in plaintext with I
    for char in plainText:
      if char == 'J':
        char = 'I'
      fixedPlainText.append(char)
    
    # Insert X if pair occurs
    for i in range(1, len(plainText), 2):
      if fixedPlainText[i] == fixedPlainText[i-1]:
        fixedPlainText.insert(i, 'X')
        
    # Ensure length is even by appending 'Z'
    if len(fixedPlainText) % 2 != 0:
      fixedPlainText.append('X')
      
    print(fixedPlainText)
    # Create key square which contains elements from codePhrase and elements
    keySquare = []
    for char in codePhrase + alphabet:
      if char not in keySquare:
        keySquare.append(char)
    
    # Remove J if present in keySqaure
    for char in keySquare:
      if char == 'J':
        keySquare.remove('J')
    
    # 5 x 5 matrix from keySqaure elements
    matrix = [keySquare[i:i+5] for i in range(0, 25, 5)]
    
    # Encryption
    for i in range(0, len(fixedPlainText), 2):
        a, b = fixedPlainText[i], fixedPlainText[i + 1]

        # Find positions in matrix
        rowA, colA, rowB, colB = None, None, None, None
        for row in range(5):
            if a in matrix[row]:
                rowA, colA = row, matrix[row].index(a)
            if b in matrix[row]:
                rowB, colB = row, matrix[row].index(b)

        # Apply Playfair cipher rules
        if rowA == rowB:  
            cipherText += matrix[rowA][(colA + 1) % 5] + matrix[rowB][(colB + 1) % 5]
        elif colA == colB:  
            cipherText += matrix[(rowA + 1) % 5][colA] + matrix[(rowB + 1) % 5][colB]
        else: 
            cipherText += matrix[rowA][colB] + matrix[rowB][colA]
        
    return cipherText
    
    
plainText = 'WECANNOTTALKABOUTMOTLEYCRUEINTOOMUCHDETAIL'
codePhrase = 'NIKKYSIX'
print(PlayfairCode(plainText, codePhrase))
    
