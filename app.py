import streamlit as st
from streamlit_folium import st_folium
import folium
import random

# --- Waste Type Colors ---
WASTE_COLORS = {
    "Organic": "green",
    "Recyclable": "blue",
    "Hazardous": "red"
}

# --- Simulated Smart Bins Data ---
# Each bin has a location and a fill level
smart_bins = [
    {"id": "BIN001", "location": [12.9716, 77.5946], "waste_type": "Organic", "fill": 45},
    {"id": "BIN002", "location": [12.9722, 77.5965], "waste_type": "Recyclable", "fill": 70},
    {"id": "BIN003", "location": [12.9730, 77.5978], "waste_type": "Hazardous", "fill": 20},
]

# --- Streamlit App ---
st.title("Smart Waste Segregation System ♻️")
st.subheader("AI + IoT for Smarter Cities")

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Smart Bin", "Municipal Dashboard"])

# --- PAGE 1: Smart Bin (Upload and classify waste) ---
if page == "Smart Bin":
    st.header("Classify Household Waste")
    uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Waste Image", use_column_width=True)
        
        # Simulated prediction
        prediction = random.choice(["Organic", "Recyclable", "Hazardous"])
        st.success(f"Waste Type Detected: **{prediction}**")
        
        # Update random bin data to simulate real-time changes
        random_bin = random.choice(smart_bins)
        random_bin["waste_type"] = prediction
        random_bin["fill"] = min(100, random_bin["fill"] + random.randint(5, 15))
        
        st.info(f"Bin {random_bin['id']} now at {random_bin['fill']}% capacity.")

# --- PAGE 2: Municipal Dashboard (City-wide view) ---
elif page == "Municipal Dashboard":
    st.header("Municipal Waste Dashboard 🌍")
    st.write("Visualize bins, waste types, and fill levels in real-time.")

    # Create a map centered around the first bin
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=15)

    # Add each bin as a marker
    for bin_data in smart_bins:
        color = WASTE_COLORS.get(bin_data["waste_type"], "gray")

        if bin_data["fill"] >= 80:
            color = "orange"  # Yellow for almost full bins

        popup_text = f"""
        <b>Bin ID:</b> {bin_data['id']}<br>
        <b>Waste Type:</b> {bin_data['waste_type']}<br>
        <b>Fill Level:</b> {bin_data['fill']}%
        """
        folium.Marker(
            location=bin_data["location"],
            popup=popup_text,
            icon=folium.Icon(color=color, icon="trash")
        ).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)

   
