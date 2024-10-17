import torch
import numpy as np
import trimesh
from matplotlib import pyplot as plt
from pyrender import Mesh, Scene, PerspectiveCamera, DirectionalLight, OffscreenRenderer
from pyrender.constants import RenderFlags
 # Importing model loading function from model.py



def generate_body_pose_with_shape(pose_angle=0, shape_params=None):
    # Load the SMPL model using the function from model.py
    model = smplx.create(model_path='/content/_ai_image_generator/_ai_image/smpl_models', model_type='smpl', gender='female', ext='npz')
    # Implement pose generation logic
    return None  # Return dummy for now or generated pose image
    # Default shape parameters if none are provided
    if shape_params is None:
        shape_params = torch.zeros([1, 10])

    # Set the body pose
    body_pose = torch.zeros([1, 69])
    body_pose[0, 5] = pose_angle  # Adjust pose for arm/leg/head movement

    # Generate the body output with pose and shape
    output = model(body_pose=body_pose, betas=shape_params, return_verts=True)
    
    return output.vertices.detach().cpu().numpy()[0], output.joints.detach().cpu().numpy()[0]

def create_mesh(vertices):
    # Create a triangular mesh for rendering
    mesh = trimesh.Trimesh(vertices=vertices, faces=model.faces)
    return Mesh.from_trimesh(mesh)

def render_body(vertices, output_file="output_image.png"):
    # Convert vertices into a mesh
    mesh = create_mesh(vertices)

    # Create a scene to display the body
    scene = Scene()
    scene.add(mesh)

    # Add a camera
    camera = PerspectiveCamera(yfov=np.pi / 3.0)
    scene.add(camera, pose=np.eye(4))

    # Add a light source
    light = DirectionalLight(color=np.ones(3), intensity=3.0)
    scene.add(light, pose=np.eye(4))

    # Render offscreen
    renderer = OffscreenRenderer(viewport_width=512, viewport_height=512)
    color, _ = renderer.render(scene, flags=RenderFlags.RGBA)
    renderer.delete()

    # Save the rendered image
    plt.imshow(color)
    plt.axis('off')
    plt.savefig(output_file)
    plt.show()

# Shape parameters for body adjustment (optional for default shape)
shape_params = torch.tensor([[1.0, -1.0, 0.5, 0.0, 0.2, -0.5, 0.3, -0.3, 0.0, 0.1]])

# Generate body shape and pose (can be tested directly in pose_control.py if needed)
vertices, joints = generate_body_pose_with_shape(pose_angle=0.5, shape_params=shape_params)

# Render the body with the correct shape
render_body(vertices)
