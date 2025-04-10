def StationaryCount(numValues, values):
    # Write your code here
    # Sort value list
    sorted_values = sorted(values)
    match_count = 0
    # Compare values
    for i in range(numValues):
        if values[i] == sorted_values[i]:
            match_count += 1  
    
    return match_count

numValues = 5
values = [5, 2, 4, 2, 5]
count = StationaryCount(numValues, values)
print(count)