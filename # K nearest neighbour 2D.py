# K nearest neighbour 2D

def KNearestNeighbour(n, k, points):
    # Write your code here
    # Calculate squared distances from the first position to every other position
    distances = []
    first_position = points[0]
    
    # Iterate through n and assign x1, y1, x2, y2, positions
    for i in range(1, n):
        x1, y1 = first_position
        x2, y2 = points[i]
        # Calculate the squared distance
        dist_squared = (x1 - x2)**2 + (y1 - y2)**2
        # Store distance and corresponding index
        distances.append((dist_squared, i))
    # Sort distances based on the squared distance
    distances.sort()
    # Return the index of the k-th nearest neighbor (1-based k, so use k-1)
    return distances[k-1][1]