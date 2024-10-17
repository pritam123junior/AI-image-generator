from diffusers import StableDiffusionPipeline
import torch

def load_text_to_image_model():
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Load the model with FP16 precision (half precision)
    pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipeline.to(device)
    
    return pipeline
