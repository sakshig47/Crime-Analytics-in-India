import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Crime Analytics Dashboard",
    page_icon="🚔",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🚔 Crime Analytics Dashboard")
st.markdown("### Analyze crime trends across different cities in India")

# ---------------- LOAD DATA ----------------
# Temporary: Read cleaned CSV
# Later we'll replace this with MySQL

df = pd.read_csv("cleaned_crime_dataset.csv")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔍 Filters")

city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["city"].unique().tolist())
)

crime_domain = st.sidebar.selectbox(
    "Crime Domain",
    ["All"] + sorted(df["crime_domain"].unique().tolist())
)

gender = st.sidebar.selectbox(
    "Victim Gender",
    ["All"] + sorted(df["victim_gender"].unique().tolist())
)

age_group = st.sidebar.selectbox(
    "Age Group",
    ["All"] + sorted(df["age_group"].unique().tolist())
)

crime_time = st.sidebar.selectbox(
    "Crime Occurred",
    ["All"] + sorted(df["crime_occurred"].unique().tolist())
)

# ---------------- FILTER DATA ----------------
filtered_df = df.copy()

if city != "All":
    filtered_df = filtered_df[filtered_df["city"] == city]

if crime_domain != "All":
    filtered_df = filtered_df[filtered_df["crime_domain"] == crime_domain]

if gender != "All":
    filtered_df = filtered_df[filtered_df["victim_gender"] == gender]

if age_group != "All":
    filtered_df = filtered_df[filtered_df["age_group"] == age_group]

if crime_time != "All":
    filtered_df = filtered_df[filtered_df["crime_occurred"] == crime_time]

# ---------------- KPI CARDS ----------------
st.markdown("## 📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Crimes", len(filtered_df))
col2.metric("Cities", filtered_df["city"].nunique())
col3.metric("Crime Domains", filtered_df["crime_domain"].nunique())
col4.metric("Police Deployed", int(filtered_df["police_deployed"].sum()))

# ---------------- SHOW DATA ----------------
st.markdown("## 📋 Crime Dataset")

st.dataframe(filtered_df, use_container_width=True)

# ---------------- DOWNLOAD BUTTON ----------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="crime_data.csv",
    mime="text/csv"
)