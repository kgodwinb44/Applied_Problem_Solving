def CatOrDog2(word):
    # Write your code here
    # Dog and Cat as set variables
    dog_char = set("dogDOG")
    cat_char = set("catCAT")
    # Match count
    cat_count = 0
    dog_count = 0
    # Check for matching characters
    for char in word:
        # Check for match in cat set
        if char in cat_char:
            # Increase cat count by 1
            cat_count += 1
        # Check for match in dog set
        elif char in dog_char:
            # Increase dog count by 1
            dog_count += 1
    # Compare count values
    if cat_count > dog_count:
        return 'CAT'
    elif dog_count > cat_count:
        return 'DOG'
    else:
        return 'NEITHER'

word = 'suggestion'
result = CatOrDog2(word)
print(result)