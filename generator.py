from model import load_text_to_image_model
from pose_control import generate_body_pose_with_shape,create_mesh,render_body
import torch

pipeline = load_text_to_image_model()

def generate_image_from_prompt(prompt, pose_image=None):
    # Generate image from text prompt
    with torch.no_grad():
        result = pipeline(prompt).images[0]
    result.save("output_image.png")  # Save the generated image
    return result