import streamlit as st
import pandas as pd

# Set up page config
st.set_page_config(page_title="The STEM Pipeline Index", page_icon="📊", layout="wide")

# Title Elements
st.title("📊 The STEM Pipeline Index")
st.subheader("An Independent Data Science Platform Tracking Female Attrition in Academic STEM")
st.markdown("---")

# Research Abstract
st.header("🔬 Research Abstract")
st.info(
    "**Objective:** This platform models the 'Leaky Pipeline' phenomenon—the systemic "
    "attrition of women from academic STEM tracks—by aggregating longitudinal data from the "
    "National Science Foundation (NSF). By analyzing historical degree completion data, "
    "this project aims to quantify equity gaps and provide predictive indicators for institutional retention."
)
st.markdown("---")

# Data Visualization Hub
st.header("📈 Data Visualization Hub")
st.write("The interactive chart below displays historical NSF data for engineering doctorates awarded in the U.S. by gender.")

# Load the data file we created
try:
    df = pd.read_csv("nsf_data.csv")
    
    # Pivot data so Streamlit can chart it easily
    chart_data = df.pivot(index='Year', columns='Gender', values='Doctorates')
    
    # Render the interactive chart
    st.line_chart(chart_data)
    st.caption("Figure 1: National Science Foundation Survey of Earned Doctorates (Engineering Subfields).")
    
except Exception as e:
    st.error("Data pipeline loading error. Please check configuration files.")

# Sidebar Info
st.sidebar.header("About the Project")
st.sidebar.write("Developed by an aspiring Undergraduate Researcher.")
st.sidebar.write("Target Institution: Johns Hopkins University")
st.sidebar.write("Data Source: NSF Survey of Earned Doctorates")
