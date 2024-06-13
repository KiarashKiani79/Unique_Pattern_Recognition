### Helper Function to Determine Direction
def get_direction(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    
    if x2 == x1 and y2 == y1 - 1:
        return 1  # South
    elif x2 == x1 + 1 and y2 == y1 - 1:
        return 2  # Southeast
    elif x2 == x1 + 1 and y2 == y1:
        return 3  # East
    elif x2 == x1 + 1 and y2 == y1 + 1:
        return 4  # Northeast
    elif x2 == x1 and y2 == y1 + 1:
        return 5  # North
    elif x2 == x1 - 1 and y2 == y1 + 1:
        return 6  # Northwest
    elif x2 == x1 - 1 and y2 == y1:
        return 7  # West
    elif x2 == x1 - 1 and y2 == y1 - 1:
        return 8  # Southwest
    return None


### Main Function to Simplify Points
def simplify_points(points):
    if not points:
        return []
    
    simplified_points = []  
    current_direction = None

    for i in range(1, len(points)):
        direction = get_direction(points[i-1], points[i])
        if direction != current_direction:
            simplified_points.append(points[i-1])
            current_direction = direction
    simplified_points.append(points[-1])
    
    return simplified_points
    
print("Helper Functions To Simplyfy Data Points Loaded Successfully!")

