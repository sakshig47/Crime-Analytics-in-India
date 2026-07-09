import streamlit as st
import plotly.express as px
import pandas as pd


# =====================================================
# COMMON LAYOUT
# =====================================================

CHART_HEIGHT = 420


# =====================================================
# TOP CITIES
# =====================================================

def top_city_chart(df):

    city_df = (
        df.groupby("city")
        .size()
        .reset_index(name="Total Crimes")
        .sort_values("Total Crimes", ascending=False)
        .head(10)
    )

    fig = px.bar(
        city_df,
        x="Total Crimes",
        y="city",
        orientation="h",
        color="Total Crimes",
        text="Total Crimes",
        color_continuous_scale="Blues"
    )

    fig.update_layout(

        title="🏙 Top 10 Cities by Crime",

        title_x=0.5,

        height=CHART_HEIGHT,

        coloraxis_showscale=False,

        yaxis_title="",

        xaxis_title="Total Crimes",

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =====================================================
# WEAPON DISTRIBUTION
# =====================================================

def weapon_chart(df):

    weapon_df = (

        df.groupby("weapon_used")

        .size()

        .reset_index(name="Cases")

    )

    fig = px.pie(

        weapon_df,

        names="weapon_used",

        values="Cases",

        hole=0.55

    )

    fig.update_layout(

        title="🔫 Weapon Distribution",

        title_x=0.5,

        height=CHART_HEIGHT

    )

    st.plotly_chart(

        fig,

        width="stretch"

    )


# =====================================================
# MONTHLY CRIME TREND
# =====================================================
def crime_domain_case_status_chart(df):

    chart_df = (
        df.groupby(["crime_domain", "case_closed"])
        .size()
        .reset_index(name="Cases")
    )

    fig = px.bar(
        chart_df,
        x="Cases",
        y="crime_domain",
        color="case_closed",
        orientation="h",
        barmode="stack",
        text="Cases",
        title="Crime Domain vs Case Status",
        color_discrete_map={
            "Yes": "#1E40AF",   # Green
            "No": "#3B82F6"     # Red
        }
    )

    fig.update_layout(
        title_x=0.5,
        height=500,
        xaxis_title="Number of Cases",
        yaxis_title="Crime Domain",
        legend_title="Case Closed",
        yaxis=dict(categoryorder="total ascending")
    )

    fig.update_traces(
        textposition="inside"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# =====================================================
# CASE STATUS
# =====================================================

def case_status_chart(df):

    status = (

        df.groupby("case_closed")

        .size()

        .reset_index(name="Cases")

    )

    fig = px.bar(

        status,

        x="case_closed",

        y="Cases",

        color="case_closed",

        text="Cases"

    )

    fig.update_layout(

        title="📂 Case Status",

        title_x=0.5,

        showlegend=False,

        height=CHART_HEIGHT

    )

    fig.update_traces(

        textposition="outside"

    )

    st.plotly_chart(

        fig,

        width="stretch"

    )

    # =====================================================
# VICTIM GENDER
# =====================================================

def gender_chart(df):

    gender_df = (
        df.groupby("victim_gender")
        .size()
        .reset_index(name="Victims")
    )

    fig = px.pie(
        gender_df,
        names="victim_gender",
        values="Victims"
    )

    fig.update_layout(
        title="👤 Victim Gender Distribution",
        title_x=0.5,
        height=CHART_HEIGHT
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =====================================================
# AGE GROUP
# =====================================================

def age_group_chart(df):

    age_df = (
        df.groupby("age_group")
        .size()
        .reset_index(name="Victims")
    )

    fig = px.bar(
        age_df,
        x="age_group",
        y="Victims",
        color="age_group",
        text="Victims"
    )

    fig.update_layout(
        title="🎂 Victims by Age Group",
        title_x=0.5,
        showlegend=False,
        height=CHART_HEIGHT
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =====================================================
# CRIME BY TIME
# =====================================================

def crime_time_chart(df):

    time_df = (
        df.groupby("crime_occurred")
        .size()
        .reset_index(name="Cases")
    )

    fig = px.bar(
        time_df,
        x="crime_occurred",
        y="Cases",
        color="crime_occurred",
        text="Cases"
    )

    fig.update_layout(
        title="🕒 Crime by Time of Day",
        title_x=0.5,
        showlegend=False,
        height=CHART_HEIGHT
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =====================================================
# CRIME TYPE TREEMAP
# =====================================================
def crime_type_chart(df):

    crime_df = (
        df.groupby("crime_description")
        .size()
        .reset_index(name="Cases")
        .sort_values("Cases", ascending=False)
        .head(15)
    )

    fig = px.treemap(
        crime_df,
        path=["crime_description"],
        values="Cases",
        color="Cases",
        color_continuous_scale="Reds"
    )

    fig.update_traces(
        textinfo="label+value",
        textfont_size=14
    )

    fig.update_layout(
        title="🌳 Top Crime Types",
        title_x=0.5,
        height=CHART_HEIGHT
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # =====================================================
# SHOW ALL CHARTS
# =====================================================

def show_charts(filtered_df):

    st.subheader("📊 Crime Analytics")

    # Create Tabs
    tab1, tab2 = st.tabs([
        "📊 Overview",
        "📈 Advanced Analytics"
    ])

    # ==========================
    # TAB 1
    # ==========================

    with tab1:

        col1, col2 = st.columns(2)

        with col1:
            top_city_chart(filtered_df)

        with col2:
            crime_type_chart(filtered_df)

        st.divider()

        col3, col4 = st.columns(2)

        with col3:
            crime_domain_case_status_chart(filtered_df)

        with col4:
            crime_time_chart(filtered_df)

    # ==========================
    # TAB 2
    # ==========================

    with tab2:

        col5, col6 = st.columns(2)

        with col5:
            weapon_chart(filtered_df)

        with col6:
            age_group_chart(filtered_df)

        st.divider()

        col7, col8 = st.columns(2)

        with col7:
            gender_chart(filtered_df)

        with col8:
            case_status_chart(filtered_df)