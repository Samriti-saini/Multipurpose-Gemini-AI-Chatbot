import google.generativeai as genai

# 🔴 Paste YOUR API key here
genai.configure(api_key="enter your api key")

print("Available models that support text generation:\n")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)
