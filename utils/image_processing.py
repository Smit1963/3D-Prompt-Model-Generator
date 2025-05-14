from rembg import remove
from PIL import Image
import numpy as np
import trimesh

def remove_background(image):
    return remove(image)

def convert_to_3d(image):
    # Remove background
    output = remove_background(image)
    # Convert to grayscale for simplicity
    output = output.convert('L')
    # Simulate 3D conversion (extrude silhouette)
    # This is a placeholder - in a real app, use depth estimation or other methods
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                          [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    faces = np.array([[0, 1, 2], [0, 2, 3], [4, 5, 6], [4, 6, 7],
                       [0, 1, 5], [0, 5, 4], [2, 3, 7], [2, 7, 6],
                       [0, 3, 7], [0, 7, 4], [1, 2, 6], [1, 6, 5]])
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    return mesh 