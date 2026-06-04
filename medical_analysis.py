from gemini_chatbot import vision

def analyze_medical_image(image):
    return vision(
        "Analyze this medical image and give a general observation. Do not make a diagnosis.",
        image
    )
