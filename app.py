import streamlit as st

st.set_page_config(page_title="Flood Risk Mapping Using QGIS", layout="wide")

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

local_css("style.css")

# HEADER
st.markdown("<h1 class='title'>Flood Risk Mapping Using QGIS</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>A Geospatial Approach for Identifying and Analysing Flood-Prone Areas</h3>", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📌 Presentation Menu")

section = st.sidebar.radio(
    "Navigate Sections",
    [
        "Home", "Aim", "Objectives", "Keywords", "Abstract",
        "Introduction", "Literature Review", "Problem Statement",
        "Study Area", "Data & Materials", "Methodology",
        "QGIS Implementation", "Map View",
        "Analysis & Results",
        "Discussion", "Recommendations", "Conclusion"
    ]
)

# ---------------- HOME ----------------
if section == "Home":
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3e/Flooded_area.jpg",
        use_container_width=True
    )

    st.markdown("""
    ## 🌊 Welcome to Flood Risk Mapping Project

    Floods are one of the most destructive natural disasters causing:

    - Loss of life  
    - Damage to infrastructure  
    - Agricultural loss  
    - Economic disruption  

    This project demonstrates how **QGIS and GIS techniques** are used to identify flood-prone areas scientifically.
    """)

# ---------------- AIM ----------------
elif section == "Aim":
    st.header("🎯 Aim")
    st.markdown("""
    To develop a scientifically accurate flood risk map using GIS integrating DEM, rainfall, LULC and drainage data.
    """)

# ---------------- OBJECTIVES ----------------
elif section == "Objectives":
    st.header("📌 Objectives")
    st.markdown("""
    ✔ GIS flood risk mapping  
    ✔ LULC classification  
    ✔ DEM & slope analysis  
    ✔ Drainage analysis  
    ✔ MCDA weighted overlay  
    ✔ Flood zonation mapping  
    """)

# ---------------- KEYWORDS ----------------
elif section == "Keywords":
    st.header("🔑 Keywords")
    st.markdown("Flood Risk Mapping, QGIS, GIS, DEM, LULC, MCDA, Remote Sensing")

# ---------------- ABSTRACT ----------------
elif section == "Abstract":
    st.header("📝 Abstract")
    st.markdown("""
    This study uses QGIS and spatial datasets to analyze flood risk using weighted overlay technique and classify zones into high, moderate, and low risk.
    """)

# ---------------- INTRODUCTION ----------------
elif section == "Introduction":
    st.header("📖 Introduction")
    st.markdown("""
    Floods occur due to rainfall, river overflow and urbanization. GIS helps in analyzing and predicting flood-prone areas.
    """)

# ---------------- LITERATURE REVIEW ----------------
elif section == "Literature Review":
    st.header("📚 Literature Review")
    st.markdown("""
    Previous studies show elevation, rainfall, and urbanization strongly influence flood risk.
    """)

# ---------------- PROBLEM ----------------
elif section == "Problem Statement":
    st.header("⚠️ Problem Statement")
    st.markdown("""
    Flood risk is influenced by poor drainage, urbanization, low elevation and climate change.
    """)

# ---------------- STUDY AREA ----------------
elif section == "Study Area":
    st.header("🌍 Study Area")
    st.markdown("""
    Includes city/district/river basin with elevation, rainfall and drainage systems.
    """)

# ---------------- DATA ----------------
elif section == "Data & Materials":
    st.header("🗂 Data & Materials")
    st.markdown("""
    DEM, Satellite Images, Rainfall Data, Drainage Maps, Soil Data
    """)

# ---------------- METHODOLOGY ----------------
elif section == "Methodology":
    st.header("⚙️ Methodology")
    st.markdown("""
    Data collection → preprocessing → analysis → MCDA → final flood map
    """)

# ---------------- QGIS ----------------
elif section == "QGIS Implementation":
    st.header("🛰 QGIS Steps")
    st.markdown("""
    Import data → CRS setup → LULC → slope → buffers → raster overlay → final map
    """)

# ---------------- MAP VIEW ----------------
elif section == "Map View":
    st.header("🗺 Interactive Flood Risk Map")

    import folium
    from streamlit_folium import st_folium

    m = folium.Map(location=[19.07, 72.87], zoom_start=11)

    folium.Circle(
        location=[19.10, 72.85],
        radius=2000,
        color="red",
        fill=True,
        fill_opacity=0.5,
        popup="High Risk Zone"
    ).add_to(m)

    folium.Circle(
        location=[19.12, 72.90],
        radius=2500,
        color="orange",
        fill=True,
        fill_opacity=0.4,
        popup="Moderate Risk Zone"
    ).add_to(m)

    folium.Circle(
        location=[19.05, 72.92],
        radius=3000,
        color="green",
        fill=True,
        fill_opacity=0.3,
        popup="Low Risk Zone"
    ).add_to(m)

    st_folium(m, width=900, height=600)

# ---------------- RESULTS ----------------
elif section == "Analysis & Results":
    st.header("📊 Results")
    st.markdown("""
    Low elevation + high rainfall = high flood risk zones identified.
    """)

# ---------------- DISCUSSION ----------------
elif section == "Discussion":
    st.header("💬 Discussion")
    st.markdown("""
    GIS improves flood prediction accuracy but depends on data quality.
    """)

# ---------------- RECOMMENDATIONS ----------------
elif section == "Recommendations":
    st.header("📌 Recommendations")
    st.markdown("""
    Improve drainage, afforestation, early warning systems and GIS monitoring.
    """)

# ---------------- CONCLUSION ----------------
elif section == "Conclusion":
    st.header("✅ Conclusion")
    st.markdown("""
    QGIS-based flood risk mapping is effective for disaster management and planning.
    """)