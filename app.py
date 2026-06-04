import streamlit as st
from PIL import Image
from gemini_chatbot import chat
from image_captioning import caption_image
from medical_analysis import analyze_medical_image
from disease_detection import predict_disease

st.set_page_config(page_title="MultiPurpose Gemini Based AI Model", layout="wide")

st.markdown("""
<style>
/* Main app background (unchanged) */
.stApp { 
    background-color:#0b0f1a; 
    color:white; 
}

/* Sidebar background (unchanged) */
[data-testid="stSidebar"] { 
    background:#121628; 
}

/* Make sidebar text bright white ONLY */
[data-testid="stSidebar"] * {
    color: #ffffff !important;
    font-weight: 700;
}

/* Buttons (unchanged) */
.stButton > button { 
    background:#e63946; 
    color:white; 
    border-radius:8px; 
}
</style>
""", unsafe_allow_html=True)



st.sidebar.markdown("## 🤖 MultiPurpose Gemini Based AI Model")

menu = st.sidebar.radio("", [
    "💬 ChatBot",
    "🖼 Image Captioning",
    "❓ Ask Me Anything",
    "🩺 Medical Image Detection",
    "❤️ Health Diagnosis"
])

# ---------------- CHATBOT ----------------
if menu == "💬 ChatBot":
    st.header("💬 Gemini ChatBot")
    q = st.text_input("Ask something")
    if st.button("Send"):
        st.write(chat(q))

# ---------------- IMAGE CAPTIONING ----------------
elif menu == "🖼 Image Captioning":
    st.header("📸 Snap Narrate")
    img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if img:
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(img), use_column_width=True)
        with col2:
            if st.button("Generate Caption"):
                st.write(caption_image(img))

# ---------------- ASK ME ANYTHING ----------------
elif menu == "❓ Ask Me Anything":
    st.header("❓ Ask Me Anything")
    q = st.text_area("Ask your question")
    if st.button("Get Answer"):
        st.write(chat(q))

# ---------------- MEDICAL IMAGE ----------------
elif menu == "🩺 Medical Image Detection":
    st.header("🩺 Medical Image Detection")
    img = st.file_uploader("Upload medical image", type=["jpg", "jpeg", "png"])
    if img:
        st.image(Image.open(img), width=300)
        st.warning(analyze_medical_image(img))

# ---------------- DISEASE PREDICTION ----------------
elif menu == "❤️ Health Diagnosis":
    st.header("❤️ Multi-Disease Prediction")
    age = st.slider("Age", 1, 100, 30)
    bp = st.slider("Blood Pressure", 60, 200, 120)
    sugar = st.slider("Blood Sugar", 60, 300, 120)

    if st.button("Predict"):
        st.success(predict_disease(age, sugar, bp))
