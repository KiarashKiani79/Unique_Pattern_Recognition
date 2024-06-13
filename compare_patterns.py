from simplify_points import simplify_points
from affine_transform import calculate_affine_transform

### Compare pattern's scales, rotations, and translations
# using the affine transformation
def are_they_same_patterns (transformations):
    scalingx = round(transformations['scaling_x'],2)
    scalingy = round(transformations['scaling_y'],2)
    rotation = round(transformations['rotation_angle_degrees'],0)
    translationx = round(transformations['translation_x'],0)
    translationy = round(transformations['translation_y'],0)
    if scalingx != scalingy:
        print("Patterns are not the same")
        return False
    else:
        if scalingx == 1 :
            print(f"***\nPatterns are the same with: \n({rotation} degrees) rotation\n({translationx}, {translationy}) translation")
        else:
            print(f"***\nPatterns are the same with: \n({scalingx} scaling) \n({rotation} degrees) rotation \n({translationx}, {translationy}) translation\n***")
        return True

# Check if the number of edges in the simplified patterns are equal    
def number_of_edges_are_equal (src, dst):
    if len(src) != len(dst):
        print("Number of edges in simplified patterns are not equal")
        return False
    else:
        return True
    
# Check if the patterns are identical 
# by comparing their simplified points
# Return True if they are identical  
def patterns_are_identical (src_points, dst_points):
    src = simplify_points(src_points)
    dst = simplify_points(dst_points)
    if not number_of_edges_are_equal(src,dst):
        return False
    if len(src) == 2 or len(dst)==2:
        return True
    else:
        transformations = calculate_affine_transform(src,dst)
        return are_they_same_patterns(transformations)
    
    
def invert(tuples_list):
    # Reverse the order of the tuples in the list
    reversed_list = tuples_list[::-1]
    return reversed_list


print("Helper Functions For Comparing Patterns Loaded Successfully!")