# 3D Model Generator

This project is a prototype that converts a photo or text prompt into a simple 3D model (.obj). It uses Streamlit for the web interface, rembg for background removal, and trimesh/pyrender for 3D visualization.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Run the Streamlit app:
```
streamlit run main.py
```

## Usage

- **Image Input:** Upload a .jpg or .png file. The app will remove the background and generate a 3D model.
- **Text Input:** Enter a text prompt (e.g., "A small toy car") to generate a 3D model.

## Libraries Used

- **Streamlit:** For the web interface.
- **rembg:** For background removal.
- **Pillow:** For image handling.
- **trimesh:** For 3D mesh manipulation.
- **matplotlib:** For 3D visualization.

## Approach

- **Image Processing:** The app uses rembg to remove the background from uploaded images. **Currently, the 3D model generation is a placeholder and always returns a simple cube, regardless of the input image.**
- **Text-to-3D:** The function for text-to-3D is also a placeholder and always returns a simple cube, regardless of the prompt. **This is for demonstration purposes only.**
- **Output:** The generated 3D model is saved as a .obj file and visualized using matplotlib.

## Why Only a Cube is Generated

- Generating a real 3D model from a single image or a text prompt is a complex AI/ML task.
- The current implementation uses a hardcoded cube as a placeholder to demonstrate the pipeline and UI.
- This ensures the app's upload, download, and visualization features work as expected.

## How to Generate Real 3D Models

- **Text-to-3D:** Integrate an open-source model like [Shap-E](https://github.com/openai/shap-e) or [DreamFusion](https://github.com/ashawkey/stable-dreamfusion). These require a GPU and a more complex setup.
- **Image-to-3D:** Use a depth estimation model (like MiDaS) to estimate depth from the image, then create a mesh from the depth map. Or, use silhouette-based extrusion for simple objects.

## Note

This is a prototype. For production, integrate a robust text-to-3D model (e.g., Shap-E) and improve the image-to-3D conversion logic. See the comments in the code for where to add these improvements. 