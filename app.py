import streamlit as st
import pandas as pd

# Import Components
from Dashboard.sidebar import sidebar
from Dashboard.kpi import show_kpis
from Dashboard.charts import show_charts
from GenAI.chartbot import ask_ai

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

df = pd.read_csv("cleaned_crime_dataset.csv")

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

left, right = st.columns([3.5,1.2], gap="medium")

# ===========================
# LEFT SIDE
# ===========================

with left:

    # KPI SECTION
    show_kpis(filtered_df)

    st.divider()

    # CHART PLACEHOLDER

    show_charts(filtered_df)

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

    # Chat history persists across reruns for this session
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_area(
        "Ask a question",
        placeholder="Example:\nWhich city has the highest crime?",
        height=150
    )

    if st.button("Send", use_container_width=True):

        if not user_question.strip():
            st.warning("Please type a question first.")
        else:
            with st.spinner("Thinking..."):
                try:
                    result, explanation = ask_ai(user_question)
                    st.session_state.chat_history.append(
                        {
                            "question": user_question,
                            "result": result,
                            "explanation": explanation,
                            "error": None,
                        }
                    )
                except Exception as e:
                    st.session_state.chat_history.append(
                        {
                            "question": user_question,
                            "result": None,
                            "explanation": None,
                            "error": str(e),
                        }
                    )

    st.divider()

    # Show most recent answer first
    for chat in reversed(st.session_state.chat_history):

        st.markdown(f"**🧑 You:** {chat['question']}")

        if chat["error"]:
            st.error(chat["error"])
        else:
            result = chat["result"]

            if isinstance(result, (pd.DataFrame, pd.Series)):
                st.dataframe(result, use_container_width=True)
            else:
                st.success(f"**Result:** {result}")

            st.markdown(f"**🤖 Explanation:** {chat['explanation']}")

        st.divider()