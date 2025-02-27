import streamlit as st
from PIL import Image

# Dark Mode Toggle
dark_mode = st.toggle("🌙 Dark Mode")


# Apply custom styling based on dark mode
if dark_mode:
    st.markdown(
        """
        <style>
            /* Background & Text */
            body, .stApp { background-color: black !important; color: white !important; }
            
            /* Headings */
            h1, h2, h3, h4, h5, h6, p, label { color: white !important; }

            /* Buttons */
            .stButton>button { background-color: #4CAF50 !important; color: white !important; border-radius: 10px; }
            /* Selectbox */
            .stSelectbox>div, .stNumberInput>div, .stTextInput>div { background-color: #222 !important; color: white !important; border-radius: 10px; }

            /* Success Message */
            .stAlert { background-color: #333 !important; color: white !important; border-radius: 10px; }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
            /* Background & Text */
            body, .stApp { background-color: white !important; color: black !important; }
            
            /* Headings */
            h1, h2, h3, h4, h5, h6, p, label { color: black !important; }

            /* Buttons */
            .stButton>button { background-color: skyblue !important; color: white !important; border-radius: 10px; }

            /* Selectbox */
            .stSelectbox>div, .stNumberInput>div, .stTextInput>div { background-color: #f1f1f1 !important; color: black !important; border-radius: 10px; }

            /* Success Message */
            .stAlert { background-color: #ddd !important; color: black !important; border-radius: 10px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Title

st.markdown("<h1 style='text-align: center; font-size: 36px;'>Unit Convertor</h1>", unsafe_allow_html=True)

# Dictionary for unit conversion
to_meters = {
    "Meter (m)": 1.0,
    "Kilometer (km)": 1000.0,
    "Mile (mi)": 1609.34,
    "Foot (ft)": 0.3048,
    "Yard (yd)": 0.9144
}

units = list(to_meters.keys())

st.write("### 📏 Convert between different units of length")

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit:", units)
with col2:
    to_unit = st.selectbox("To Unit:", units)

value = st.number_input("Enter the value:", min_value=0.0, value=1.0)

if st.button("Convert 🔄"):
    value_in_meters = value * to_meters[from_unit]
    converted_value = value_in_meters / to_meters[to_unit]
    st.success(f"✅ {value} {from_unit} = {converted_value:.4f} {to_unit}")
