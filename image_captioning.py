from gemini_chatbot import vision


def caption_image(image):
    return vision(
        "Describe this image in detail.",
        image
    )
