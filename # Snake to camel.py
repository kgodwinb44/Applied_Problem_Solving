# Snake to camel
# E.g. Var_name_1 = varName1

def SnakeToCamel(S):
   
    # Count and extract leading underscores
    leading_underscores = ''
    i = 0
    while i < len(S) and S[i] == '_':
        leading_underscores += '_'
        i += 1
    
    # Process the rest of the string
    parts = S[i:].split('_')
    camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    # Preserve leading underscores
    return leading_underscores + camel_case

s = "var_name_1"
print(SnakeToCamel(s))