import streamlit as st

# Set up the page appearance
st.set_page_config(page_title="The STEM Pipeline Index", page_icon="📊", layout="wide")

# Main Header (The Ivy League Hook)
st.title("📊 The STEM Pipeline Index")
st.subheader("An Independent Data Science Platform Tracking Female Attrition in Academic STEM")

st.markdown("---")

# The Academic Abstract (What Johns Hopkins looks for)
st.header("🔬 Research Abstract")
st.info(
    "**Objective:** This platform models the 'Leaky Pipeline' phenomenon—the systemic "
    "attrition of women from academic STEM tracks—by aggregating longitudinal data from the "
    "National Science Foundation (NSF). By analyzing historical degree completion and career "
    "placement data, this project aims to quantify equity gaps and provide predictive indicators "
    "for institutional retention."
)

st.markdown("---")

# Temporary Placeholder for our Interactive Charts
st.header("📈 Data Visualization Hub")
st.warning("Data pipelines are currently initializing. Interactive charts will appear below.")

# Sidebar info
st.sidebar.header("About the Project")
st.sidebar.write("Developed by an aspiring Undergraduate Researcher.")
st.sidebar.write("Data Source: NSF Survey of Earned Doctorates")
