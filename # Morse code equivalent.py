# Morse code equivalent

def MorseEquivalent(A, B):
    # Write your code here - print TRUE if A and B are equivalent FALSE otherwise
    
    # Covert A and B into morse
    A_morse = []
    B_morse = []

    morse_code_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',  
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',  
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',  
    'z': '--..'}
    
    # Convert A and B into morse
    for char in A:
        A_morse.append(morse_code_dict[char])
    for char in B:
        B_morse.append(morse_code_dict[char])
    
    print(''.join(A_morse))
    print(''.join(B_morse))
    # If morse is equal without spaces, then it must be true
    # ''.join changes from list to string with no spaces
    if ''.join(A_morse) == ''.join(B_morse):
        print("TRUE")
    else:
        print("FALSE")
    
A = ['abc']
B = ['wske']
print(MorseEquivalent(A,B))

