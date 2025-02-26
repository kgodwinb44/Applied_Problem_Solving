# Taking steps

def TakeSteps(nArray, nSteps, grid):
    # Write your code here
    
    x, y = 0, 0
    i = 0
    
    while i < nSteps:
        move = grid[y][x]
        print(grid)
        
        if move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y -= 1
        elif move == 'v':
            y += 1
        i += 1
    return nArray * y + x
       
nArrray = 8
nSteps = 25
grid = ['>>>v>>>v', '^v<v^v<<', '^v^>^>>v', '^v^<<<<<', '^>>v>>>v', '^<<v^v<<', '>>^>^>>v', '^<<<<<<<']
print(TakeSteps(nArrray, nSteps, grid))