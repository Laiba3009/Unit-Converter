import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container  # type: ignore

# Custom Styling
st.markdown(
    """
    <style>
        .main-title {
            color: #4CAF50;
            text-align: center;
            font-size: 65px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: blue;
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
        .stSelectbox>div {
            background-color: #f1f1f1;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
