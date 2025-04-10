# Guided Binary Search

def GuidedSearch(N, values, pattern, nSearch):
    # Initial bounds
    low = 0
    high = N - 1

    # Perform nSearch operations
    for _ in range(nSearch):
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Check the rightmost bit of the pattern (0 or 1)
        if pattern % 2 == 1:
            # If the bit is 1, move to the upper half
            low = mid + 1
        else:
            # If the bit is 0, move to the lower half
            high = mid - 1
        
        # Right shift the pattern by 1 to check the next bit
        pattern //= 2

    # Return the value at the final index `low`
    return values[low]