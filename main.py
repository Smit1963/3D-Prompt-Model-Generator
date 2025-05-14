import streamlit as st
import os
from PIL import Image
import io
import trimesh
import pyrender
import numpy as np
import tempfile
from utils.image_processing import convert_to_3d
from utils.text_to_3d import text_to_3d

# Function to save mesh as .obj
def save_mesh(mesh, filename):
    mesh.export(filename)

# Function to visualize mesh using pyrender
def visualize_mesh(mesh):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.vertices[:, 0], mesh.vertices[:, 1], mesh.vertices[:, 2], triangles=mesh.faces)
    st.pyplot(fig)
    return fig

# Streamlit UI
st.title('3D Model Generator')
st.write('Upload an image or enter a text prompt to generate a 3D model.')

# Input options
input_type = st.radio('Choose input type:', ['Image', 'Text'])

if input_type == 'Image':
    uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Generate 3D Model'):
            mesh = convert_to_3d(image)
            with tempfile.NamedTemporaryFile(suffix='.obj', delete=False) as tmp:
                save_mesh(mesh, tmp.name)
                st.download_button('Download .obj file', open(tmp.name, 'rb'), file_name='model.obj')
            st.write('Visualizing 3D model...')
            visualize_mesh(mesh)
else:
    text_input = st.text_input('Enter a text prompt:', 'A small toy car')
    if st.button('Generate 3D Model'):
        mesh = text_to_3d(text_input)
        with tempfile.NamedTemporaryFile(suffix='.obj', delete=False) as tmp:
            save_mesh(mesh, tmp.name)
            st.download_button('Download .obj file', open(tmp.name, 'rb'), file_name='model.obj')
        st.write('Visualizing 3D model...')
        visualize_mesh(mesh) 