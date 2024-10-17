import gradio as gr
from generator import generate_image

# Add Textbox for natural language prompt
prompt_input = gr.Textbox(
    placeholder="Enter prompt (e.g. 'arms raised', 'slightly bent knees')", 
    label="Text Prompt"
)

# Create Gradio interface
gr.Interface(
    fn=generate_image,
    inputs=[prompt_input],
    outputs=gr.Image(type="filepath"),  # Output as filepath
    live=True,
).launch()
