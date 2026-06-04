import google.generativeai as genai
from PIL import Image

# ✅ Paste your API key
genai.configure(api_key="enter your api key")

# ✅ Text model (stable)
text_model = genai.GenerativeModel("gemini-2.0-flash-001")

# ✅ Vision model (same model also supports images)
vision_model = genai.GenerativeModel("gemini-2.0-flash-001")

def chat(prompt):
    try:
        if not prompt.strip():
            return "Please enter a question."
        response = text_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"ERROR: {e}"

def vision(prompt, image_file):
    try:
        image = Image.open(image_file)
        response = vision_model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"ERROR: {e}"
