# Cat and mouse

def catAndMouse(x, y, z):
    # Write your code here
    # Distances
    cat_A_distance = z - x
    cat_B_distance = z - y
    # Check who has the smaller distance
    if abs(cat_A_distance) < abs(cat_B_distance):
        return 'Cat A'
    elif abs(cat_B_distance) < abs(cat_A_distance):
        return 'Cat B'
    else:
        return 'Mouse C'
       
x = 1
y = 3
z = 2
catAndMouse(x,y,z)