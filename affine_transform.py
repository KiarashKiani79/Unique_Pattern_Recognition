import numpy as np

def calculate_affine_transform(src_points, dst_points):
    # Convert points to numpy arrays if they are not already
    src_points = np.array(src_points)
    dst_points = np.array(dst_points)

    # Ensure the points arrays are of the same shape
    assert src_points.shape == dst_points.shape, "Source and destination points must have the same shape"

    num_points = src_points.shape[0]
    assert num_points >= 3, "At least 3 points are required to compute an affine transform"

    # Construct the matrices A and B for the equation A * T = B
    A = np.zeros((2 * num_points, 6))
    B = np.zeros((2 * num_points))

    for i in range(num_points):
        A[2 * i] = [src_points[i, 0], src_points[i, 1], 1, 0, 0, 0]
        A[2 * i + 1] = [0, 0, 0, src_points[i, 0], src_points[i, 1], 1]
        B[2 * i] = dst_points[i, 0]
        B[2 * i + 1] = dst_points[i, 1]

    # Solve the least squares problem to find the transformation matrix T
    T, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
    
    # Extract the affine transformation matrix
    M = np.array([
        [T[0], T[1], T[2]],
        [T[3], T[4], T[5]],
        [0, 0, 1]
    ])

    # Extract the linear transformation components
    a, b, tx = M[0]
    c, d, ty = M[1]
    
    # Calculate the scaling factors
    scale_x = np.sqrt(a**2 + b**2)
    scale_y = np.sqrt(c**2 + d**2)
    
    # Calculate the rotation angle in degrees
    rotation_angle = np.arctan2(b, a) * 180 / np.pi
    
    # Output the transformations
    transformations = {
        "affine_matrix": M[:2],  # Return only the 2x3 matrix for consistency
        "scaling_x": scale_x,
        "scaling_y": scale_y,
        "rotation_angle_degrees": rotation_angle,
        "translation_x": tx,
        "translation_y": ty
    }
    
    return transformations

print("Affine Transformation Function Loaded Successfully!")
