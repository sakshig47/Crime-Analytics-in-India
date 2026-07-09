import streamlit as st


def sidebar(df):
    """
    Displays sidebar filters and returns the filtered dataframe.
    """

    st.sidebar.title("🚔 Crime Analytics")

    st.sidebar.markdown("---")

    st.sidebar.header("Filters")

    # -------------------------------
    # CITY
    # -------------------------------

    city = st.sidebar.selectbox(
        "🏙 City",
        ["All"] + sorted(df["city"].dropna().unique().tolist())
    )

    # -------------------------------
    # CRIME DOMAIN
    # -------------------------------

    crime_domain = st.sidebar.selectbox(
        "📂 Crime Domain",
        ["All"] + sorted(df["crime_domain"].dropna().unique().tolist())
    )

    # -------------------------------
    # CRIME TYPE
    # -------------------------------

    crime_type = st.sidebar.selectbox(
        "⚖ Crime Type",
        ["All"] + sorted(df["crime_description"].dropna().unique().tolist())
    )

    # -------------------------------
    # GENDER
    # -------------------------------

    gender = st.sidebar.selectbox(
        "👤 Victim Gender",
        ["All"] + sorted(df["victim_gender"].dropna().unique().tolist())
    )

    # -------------------------------
    # AGE GROUP
    # -------------------------------

    age_group = st.sidebar.selectbox(
        "🎂 Age Group",
        ["All"] + sorted(df["age_group"].dropna().unique().tolist())
    )

    # -------------------------------
    # CRIME TIME
    # -------------------------------

    crime_time = st.sidebar.selectbox(
        "🕒 Crime Occurred",
        ["All"] + sorted(df["crime_occurred"].dropna().unique().tolist())
    )

    # -------------------------------
    # WEAPON
    # -------------------------------

    weapon = st.sidebar.selectbox(
        "🔫 Weapon Used",
        ["All"] + sorted(df["weapon_used"].dropna().unique().tolist())
    )

    # -------------------------------
    # CASE CLOSED
    # -------------------------------

    case_closed = st.sidebar.selectbox(
        "✅ Case Closed",
        ["All"] + sorted(df["case_closed"].dropna().unique().tolist())
    )

    st.sidebar.markdown("---")

    st.sidebar.success("Filters Applied")

    # =====================================
    # FILTER DATA
    # =====================================

    filtered_df = df.copy()

    if city != "All":
        filtered_df = filtered_df[
            filtered_df["city"] == city
        ]

    if crime_domain != "All":
        filtered_df = filtered_df[
            filtered_df["crime_domain"] == crime_domain
        ]

    if crime_type != "All":
        filtered_df = filtered_df[
            filtered_df["crime_description"] == crime_type
        ]

    if gender != "All":
        filtered_df = filtered_df[
            filtered_df["victim_gender"] == gender
        ]

    if age_group != "All":
        filtered_df = filtered_df[
            filtered_df["age_group"] == age_group
        ]

    if crime_time != "All":
        filtered_df = filtered_df[
            filtered_df["crime_occurred"] == crime_time
        ]

    if weapon != "All":
        filtered_df = filtered_df[
            filtered_df["weapon_used"] == weapon
        ]

    if case_closed != "All":
        filtered_df = filtered_df[
            filtered_df["case_closed"] == case_closed
        ]

    return filtered_df