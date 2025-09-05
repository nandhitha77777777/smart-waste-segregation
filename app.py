import streamlit as st
from PIL import Image
import random

st.title("🌱 Smart Waste Segregation System")
st.write("Upload an image of waste to classify it as Organic, Recyclable, or Hazardous.")
st.markdown("---")

points_dict = {
    "Organic": 5,
    "Recyclable": 10,
    "Hazardous": 15
}

bin_fill = random.randint(10, 90)

uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Waste Item", use_column_width=True)

    labels = ["Organic", "Recyclable", "Hazardous"]
    prediction = random.choice(labels)

    st.success(f"**Prediction:** {prediction}")
    st.metric("Points Earned", points_dict[prediction])

    st.progress(bin_fill / 100)
    st.caption(f"Bin Fill Level: {bin_fill}%")

    st.markdown("### 🎁 Rewards Earned")
    if prediction == "Organic":
        st.write("🌱 Composting credits: 1 point")
    elif prediction == "Recyclable":
        st.write("♻️ Recycling credits: 2 points")
    else:
        st.write("⚠️ Safe disposal credits: 3 points")
