import streamlit as st
import pandas as pd


def show_kpis(filtered_df):
    

    st.subheader("📊 KPI's")

    # ==========================
    # KPI Calculations
    # ==========================

    total_crimes = len(filtered_df)

    total_cities = filtered_df["city"].nunique()

    total_crime_types = filtered_df["crime_description"].nunique()

    avg_age = round(filtered_df["victim_age"].mean(), 1)


    closure_rate = round(
        (filtered_df["case_closed"] == "Yes").mean() * 100,
        2
    )

    solved_cases = (
        filtered_df["case_closed"] == "Yes"
    ).sum()

    unsolved_cases = (
        filtered_df["case_closed"] == "No"
    ).sum()



    # ==========================
    # KPI Row 1
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🚔 Total Crimes",
        f"{total_crimes:,}"
    )

    col2.metric(
        "🏙 Cities",
        total_cities
    )

    col3.metric(
        "📂 Crime Types",
        total_crime_types
    )

    col4.metric(
        "📋 Records Displayed",
        len(filtered_df)
    )

    st.markdown("")

    # ==========================
    # KPI Row 2
    # ==========================

    col5, col6, col7, col8 = st.columns(4)

    col5.metric(
        "👤 Avg Victim Age",
        avg_age
    )

    col6.metric(
        "✅ Solved Cases",
        solved_cases
    )

    col7.metric(
        "❌ Unsolved Cases",
        unsolved_cases
    )


    col8.metric(
        "📈 Closure Rate",
        f"{closure_rate}%"
    )
    st.markdown("")




