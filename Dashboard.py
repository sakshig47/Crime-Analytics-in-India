import streamlit as st
import pandas as pd

# Import Components
from dashboard.sidebar import sidebar
from dashboard.kpis import show_kpis

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Crime Analytics Dashboard",
    page_icon="🚔",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("data/cleaned_crime_dataset.csv")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

filtered_df = sidebar(df)

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("🚔 Crime Analytics Dashboard")

st.caption(
    "Analyze crime trends across different cities in India."
)

st.divider()

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

left, right = st.columns([5, 2], gap="large")

# ===========================
# LEFT SIDE
# ===========================

with left:

    # KPI SECTION
    show_kpis(filtered_df)

    st.divider()

    # CHART PLACEHOLDER
    st.subheader("📊 Analytics")

    chart1, chart2 = st.columns(2)

    with chart1:
        st.info("Bar Chart")

    with chart2:
        st.info("Pie Chart")

    chart3, chart4 = st.columns(2)

    with chart3:
        st.info("Line Chart")

    with chart4:
        st.info("Donut Chart")

    st.divider()

    # DATASET
    st.subheader("📋 Crime Dataset")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500
    )

    st.download_button(
        label="⬇ Download CSV",
        data=filtered_df.to_csv(index=False),
        file_name="crime_dataset.csv",
        mime="text/csv"
    )

# ===========================
# RIGHT SIDE
# ===========================

with right:

    st.subheader("🤖 AI Crime Assistant")

    st.info(
        "The AI chatbot will be integrated in the next phase."
    )

    user_question = st.text_area(
        "Ask a question",
        placeholder="Example:\nWhich city has the highest crime?",
        height=250
    )

    if st.button("Send", use_container_width=True):

        st.success("AI response will appear here.")