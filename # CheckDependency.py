def CheckDependency(numObjects, numDependencies, A, B, dependencies):
    # Write your code here
    num_path = {}
    # Create graph from dependency list
    # Check current and next value in list
    for i in range(0, len(dependencies), 2):
        # Assign current as a and next as b
        num_a = dependencies[i]
        num_b = dependencies[i + 1]
        # Check current number is not in dictionary
        if num_a not in num_path:
            # Assign its position with the item being a list
            num_path[num_a] = []
        # Else append num b into the item
        num_path[num_a].append(num_b)
    # Depth first search, use stack to check if B is reachable from A
    # Store visted nodes as set
    visited = set()
    # Start from DFS from node A
    stack = [A]
    # While stack is present
    while stack:
        # Pop last node from stack
        node = stack.pop()
        # Check if current node = B
        if node == B:
            return 'TRUE'
        # Else add node to visited
        visited.add(node)
        # Iterate through dictionary
        for path in num_path.get(node, []):
            if path not in visited:
                stack.append(path)
    return 'FALSE'
    
        

        


numObj = 10
numDep = 9
a = 8
b = 6
dependencies = [6, 7, 6, 2, 1, 3, 1, 0, 1, 4, 1, 6, 5, 9, 9, 8, 8, 1]
result = CheckDependency(numObj,numDep,a,b,dependencies)
print(result)