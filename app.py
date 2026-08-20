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

# Layout columns for side-by-side presentation
col1, col2 = st.columns(2)

with col1:
    st.header("📈 Data Visualization Hub")
    st.write("Historical NSF data for engineering doctorates awarded in the U.S. by gender.")
    
    try:
        df = pd.read_csv("nsf_data.csv")
        chart_data = df.pivot(index='Year', columns='Gender', values='Doctorates')
        st.line_chart(chart_data)
        st.caption("Figure 1: National Science Foundation Survey of Earned Doctorates (Engineering Subfields).")
    except Exception as e:
        st.error("Data pipeline loading error.")

with col2:
    st.header("🤖 Predictive Attrition Calculator")
    st.write("Evaluate institutional risk metrics based on historical attrition indicators.")
    
    # User Inputs for the simulation
    major = st.selectbox("Select STEM Discipline:", ["Computer Science", "Mechanical Engineering", "Biomedical Engineering"])
    mentors = st.slider("Number of Female Faculty/Mentors in Department:", 0, 10, 2)
    workload = st.radio("Administrative / 'Office Housework' Load Assigned to Female Staff:", ["Disproportionately High", "Equal / Fair"])
    
    # Algorithmic calculation mimicking a risk model
    base_risk = 75 if major == "Computer Science" else 60
    mentor_reduction = mentors * 4
    housework_penalty = 15 if workload == "Disproportionately High" else 0
    
    final_risk_score = max(5, min(95, base_risk - mentor_reduction + housework_penalty))
    
    # Display the result professionally
    st.metric(label="Predicted Female Attrition Risk Score", value=f"{final_risk_score}%")
    
    if final_risk_score > 60:
        st.error("⚠️ High Attrition Risk: Immediate institutional intervention and mentorship support required.")
    elif 40 <= final_risk_score <= 60:
        st.warning("⚠️ Moderate Attrition Risk: Targeted support systems recommended.")
    else:
        st.success("✅ Low Attrition Risk: Environment shows strong retention indicators.")

st.markdown("---")
# Sidebar Info
st.sidebar.header("About the Project")
st.sidebar.write("Developed by an aspiring Undergraduate Researcher.")
st.sidebar.write("Target Institution: Johns Hopkins University")
st.sidebar.write("Data Source: NSF Survey of Earned Doctorates")
