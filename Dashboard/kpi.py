import streamlit as st
import pandas as pd


def show_kpis(filtered_df):

    st.subheader("📊 Dashboard Summary")

    # ==========================
    # KPI Calculations
    # ==========================

    total_crimes = len(filtered_df)

    total_cities = filtered_df["city"].nunique()

    total_crime_types = filtered_df["crime_description"].nunique()

    avg_age = round(filtered_df["victim_age"].mean(), 1)

    avg_police = round(filtered_df["police_deployed"].mean(), 1)

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
    # Average Closing Days
    # ==========================

    closed_df = filtered_df[
        filtered_df["case_closed"] == "Yes"
    ].copy()

    if len(closed_df) > 0:

        closed_df["date_reported"] = pd.to_datetime(
            closed_df["date_reported"],
            errors="coerce",
            dayfirst=True
        )

        closed_df["date_case_closed"] = pd.to_datetime(
            closed_df["date_case_closed"],
            errors="coerce",
            dayfirst=True
        )

        avg_close_days = round(
            (
                closed_df["date_case_closed"] -
                closed_df["date_reported"]
            ).dt.days.mean(),
            1
        )

    else:

        avg_close_days = 0

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
        "👮 Avg Police",
        avg_police
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
        "📅 Avg Closing Days",
        avg_close_days
    )

    st.markdown("")

    # ==========================
    # KPI Row 3
    # ==========================

    col9, col10 = st.columns(2)

    col9.metric(
        "📈 Closure Rate",
        f"{closure_rate}%"
    )

    col10.metric(
        "📋 Records Displayed",
        len(filtered_df)
    )