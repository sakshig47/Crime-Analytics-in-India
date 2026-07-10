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

        title=dict(
            text="🏙 Top 10 Cities by Crime",
            x=0,
            xanchor="left"
        ),

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

        title=dict(
            text="🔫 Weapon Distribution",
            x=0,
            xanchor="left"
        ),

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
        title=dict(
            text="Crime Domain vs Case Status",
            x=0,
            xanchor="left"
        ),
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

        title=dict(
            text="📂 Case Status",
            x=0,
            xanchor="left"
        ),

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
        title=dict(
            text="👤 Victim Gender Distribution",
            x=0,
            xanchor="left"
        ),
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
        title=dict(
            text="🎂 Victims by Age Group",
            x=0,
            xanchor="left"
        ),
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
        title=dict(
            text="🕒 Crime by Time of Day",
            x=0,
            xanchor="left"
        ),
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
        title=dict(
            text="🌳 Top Crime Types",
            x=0,
            xanchor="left"
        ),
        height=CHART_HEIGHT
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# =====================================================
# CITY CRIME MAP & SAFETY INSIGHTS
# =====================================================

CITY_COORDINATES = {
    "Ahmedabad": (23.0225, 72.5714),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Delhi": (28.6139, 77.2090),
    "Ghaziabad": (28.6692, 77.4538),
    "Hyderabad": (17.3850, 78.4867),
    "Kolkata": (22.5726, 88.3639),
    "Lucknow": (26.8467, 80.9462),
    "Ludhiana": (30.9000, 75.8573),
    "Mumbai": (19.0760, 72.8777),
    "Nagpur": (21.1458, 79.0882),
    "Pune": (18.5204, 73.8567),
    "Surat": (21.1702, 72.8311),
    "Visakhapatnam": (17.6868, 83.2185),
    "Jaipur": (26.9124, 75.7873),
    "Indore": (22.7196, 75.8577),
    "Bhopal": (23.2599, 77.4126),
    "Coimbatore": (11.0168, 76.9558),
    "Noida": (28.5355, 77.3910),
    "Gurugram": (28.4595, 77.0266),
    "Chandigarh": (30.7333, 76.7794),
    "Kochi": (9.9312, 76.2673),
}


def build_city_summary(df):
    city_summary = (
        df.groupby("city")
        .agg(
            total_crimes=("report_number", "count"),
            solved_cases=("case_closed", lambda s: int((s == "Yes").sum())),
            unsolved_cases=("case_closed", lambda s: int((s == "No").sum()))
        )
        .reset_index()
    )

    city_summary["closure_rate"] = (
        city_summary["solved_cases"] / city_summary["total_crimes"] * 100
    ).round(1)

    city_summary["risk_score"] = (
        city_summary["total_crimes"] * (1 + city_summary["unsolved_cases"] / city_summary["total_crimes"])
    ).round(1)

    return city_summary


def city_crime_map(df):
    city_summary = build_city_summary(df)

    city_summary = city_summary[
        city_summary["city"].isin(CITY_COORDINATES.keys())
    ].copy()

    city_summary["lat"] = city_summary["city"].map(lambda city: CITY_COORDINATES[city][0])
    city_summary["lon"] = city_summary["city"].map(lambda city: CITY_COORDINATES[city][1])

    if city_summary.empty:
        st.info("No city coordinates are available for the current selection.")
        return

    fig = px.scatter_geo(
        city_summary,
        lat="lat",
        lon="lon",
        size="total_crimes",
        color="total_crimes",
        color_continuous_scale="Reds",
        hover_name="city",
        hover_data={
            "total_crimes": True,
            "solved_cases": True,
            "unsolved_cases": True,
            "closure_rate": ":.1f",
            "lat": False,
            "lon": False
        },
        size_max=40
    )

    fig.update_geos(
        showland=True,
        landcolor="rgb(245, 245, 245)",
        showcountries=True,
        countrycolor="rgb(70, 70, 70)",
        coastlinecolor="rgb(40, 40, 40)",
        showcoastlines=True,
        coastlinewidth=1.1,
        showframe=True,
        framecolor="rgb(60, 60, 60)",
        framewidth=1.2,
        projection_type="mercator",
        scope="asia",
        center=dict(lat=22.5, lon=78.96),
        lataxis_range=[6, 37],
        lonaxis_range=[68, 97]
    )

    fig.update_layout(
        title=dict(
            text="🗺 Crime Intensity by City",
            x=0,
            xanchor="left"
        ),
        margin=dict(l=20, r=20, t=70, b=20),
        height=650,
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(size=13, family="Arial"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    fig.update_traces(
        marker=dict(line=dict(width=1.5, color="rgba(0,0,0,0.35)")),
        marker_sizemin=10
    )

    st.plotly_chart(fig, use_container_width=True)


def city_safety_insights(df):
    city_summary = build_city_summary(df)

    if city_summary.empty:
        st.info("No city insights are available for the current selection.")
        return

    danger_cities = city_summary.sort_values(
        ["total_crimes", "unsolved_cases"],
        ascending=[False, False]
    ).head(5)

    safest_cities = city_summary.sort_values(
        ["total_crimes", "closure_rate"],
        ascending=[True, False]
    ).head(5)

    st.subheader("🧭 City Safety Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🚨 Higher-risk cities**")
        for _, row in danger_cities.iterrows():
            st.markdown(
                f"- **{row['city']}**: {row['total_crimes']} crimes, {row['unsolved_cases']} unsolved, {row['closure_rate']:.1f}% closure"
            )

    with col2:
        st.markdown("**🛡️ Safer cities**")
        for _, row in safest_cities.iterrows():
            st.markdown(
                f"- **{row['city']}**: {row['total_crimes']} crimes, {row['closure_rate']:.1f}% closure"
            )

    st.caption("Redder map markers indicate cities with more reported crimes; safer cities are those with lower crime counts and stronger closure rates.")


# =====================================================
# SHOW ALL CHARTS
# =====================================================

def show_charts(filtered_df):

    st.subheader("📊 Crime Analytics")

    # Create Tabs
    tab1, tab2, tab3 = st.tabs([
        "📊 Overview",
        "📈 Advanced Analytics",
        "🗺 Crime Map"
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

    # ==========================
    # TAB 3
    # ==========================

    with tab3:
        city_crime_map(filtered_df)
        st.divider()
        city_safety_insights(filtered_df)