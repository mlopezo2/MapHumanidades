import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Comunidades en el Mapa",
    page_icon="📍",
    layout="wide",
)



# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title('📍 Comunidades al Margen de las Carreteras')

# Create map data for EAFIT
yuripasse_location = pd.DataFrame({
    'lat': [1.335],
    'lon': [70.933],
    'location': ['Rio Pure']
})

# Display map
st.subheader("📍 Ubicación de los Sensores - Universidad EAFIT")
st.map(yuripasse_location, zoom=15)

