import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime

import folium
from folium.plugins import MarkerCluster

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
    'lat': [-2.2],
    'lon': [-70.3],
    'location': ['Rio Pure']
})

kubeo_location = pd.DataFrame({
    'lat': [0.6107],
    'lon': [-70.2686],
    'location': ['Aseinpome']
})

sikuani_location = pd.DataFrame({
    'lat': [3.2],
    'lon': [-70.6],
    'location': ['Orinoquía']
})

nukak_location = pd.DataFrame({
    'lat': [1.5],
    'lon': [-71.0],
    'location': ['Guaviare']
})

# Combine the two DataFrames
locations = pd.concat([yuripasse_location, kubeo_location, sikuani_location, nukak_location], ignore_index=True)


#Display map with both locations
st.subheader("Ubicación de algunas Comunidades")
st.text("En este mapa interactivo podrás explorar algunos de los puntos de ubicación aproximados de las comunidades investigadas por el proyecto. Abordamos un rango posible de ubicaciones debido a la poca información sobre la ubicación precisa de estas comunidades. ¡Explóralo libremente!")
st.map(locations, zoom=5)

# Display map
#st.subheader("📍 Ubicación de algunas comunidades")
#st.map(yuripasse_location, zoom=15)
#st.map(kubeo_location, zoom=15)




