def PathLength(numVert, numEdge, v0, v1, edges):
    # Write your code here
    num_edges = {}
    # Create graph, key as current num, item as list of edges
    for i in range(0, len(edges), 3):
        num_a = edges[i - 1]
        num_b = edges[i]
        # Check current number is not in dictionary
        if num_a not in num_edges:
            num_edges[num_a] = []
        num_edges[num_a].append(num_b)
    print(num_edges)

numVert = 10
numEdge = 9
v0 = 8
v1 = 1
edges = [0, 5, 865, 0, 6, 423, 0, 2, 947, 5, 9, 180, 5, 4, 98, 5, 8, 111, 5, 3, 658, 6, 1, 633, 2, 7, 323]
PathLength(numVert,numEdge,v0,v1,edges)