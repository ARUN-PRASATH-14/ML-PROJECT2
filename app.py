import streamlit as st
from gemini_engine import analyze_career
from db import store_result

st.set_page_config(
    page_title="AI Career Path Chooser",
    layout="centered"
)

st.title("🎓 AI Career Path Chooser")
st.write("Analyze your profile and get top career paths with roadmap")

profile = st.text_area(
    "🧠 Enter your profile",
    placeholder="""
Example:
- Skills: Python, basic ML, statistics
- Interests: AI, data, research
- Background: CSE student
- Goal: High-growth tech career
"""
)



if st.button("🚀 Analyze Career"):
    if not profile.strip():
        st.warning("Please enter your profile details")
    else:
        with st.spinner("Analyzing your career path..."):
            result = analyze_career(profile)
            store_result(profile, result)

        st.success("✅ Career Analysis Complete")
        st.markdown(result)
