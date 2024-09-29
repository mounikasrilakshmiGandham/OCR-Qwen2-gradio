import gradio as gr
from PIL import Image
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor

# Load model and processor
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct",
    torch_dtype="auto",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct"
)

# OCR extraction function
def extract_text_from_image(image):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                },
                {
                    "type": "text",
                    "text": "Extract text from the image(OCR) in its original language"
                }
            ]
        }
    ]

    text_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)

    inputs = processor(
        text=[text_prompt],
        images=[image],
        padding=True,
        return_tensors="pt"
    )
    # Uncomment this line if GPU available
    # inputs = inputs.to("cuda")
    output_ids = model.generate(**inputs, max_new_tokens=1024)

    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(inputs.input_ids, output_ids)
    ]

    extracted_text = processor.batch_decode(
        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
    )[0]

    return extracted_text

# # Keyword search function
def search_keyword(extracted_text, keyword):
    if not extracted_text:
        return "No text extracted. Please upload an image and run OCR first."
    
    if keyword:
        if keyword.lower() in extracted_text.lower():
            return f"Keyword '{keyword}' found in the extracted text."
        else:
            return f"Keyword '{keyword}' not found in the extracted text."
    return "Please enter a keyword to search."

# Combined function for OCR and keyword search
def ocr_and_search(image, keyword):
    extracted_text = extract_text_from_image(image)
    
    # If no keyword provided, return only extracted text
    if not keyword:
        return extracted_text, ""
    
    # Perform keyword search on the extracted text
    search_result = search_keyword(extracted_text, keyword)
    return extracted_text, search_result

# Gradio Interface with both OCR and keyword search
gr.Interface(
    fn=ocr_and_search,
    inputs=[gr.Image(type="pil", label="Upload Image for OCR"), 
            gr.Textbox(label="Enter keyword to search in extracted text")
            ],
    outputs=[gr.Textbox(label="Extracted Text from OCR"),
             gr.Textbox(label="Keyword Search Result")
             ],
    title="Qwen2-vl-OCR",
    description="Upload an image with Hindi and English text to extract text using OCR. (Note: The inference will be slow because we have opted for the Free-Tier (No GPU))"
).launch(share=True)