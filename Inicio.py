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
    'location': ['Aseinpome']
})

# Combine the two DataFrames
locations = pd.concat([yuripasse_location, kubeo_location, sikuani_location], ignore_index=True)

# Create a folium map centered on the average location
m = folium.Map(location=[locations['lat'].mean(), locations['lon'].mean()], zoom_start=5, tiles='Stamen Terrain')

# Add marker cluster to the map
marker_cluster = MarkerCluster().add_to(m)

# Add locations to the map with markers
for idx, row in locations.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['location']).add_to(marker_cluster)

# Render map in Streamlit
st.subheader("📍 Ubicación de algunas Comunidades")
st.write(m._repr_html_(), unsafe_allow_html=True)

# Display map with both locations
#st.subheader("📍 Ubicación de algunas Comunidades")
#st.map(locations, zoom=5)

# Display map
#st.subheader("📍 Ubicación de algunas comunidades")
#st.map(yuripasse_location, zoom=15)
#st.map(kubeo_location, zoom=15)




