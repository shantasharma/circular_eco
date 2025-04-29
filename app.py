# === app.py ===

import streamlit as st
from coordinator import run_pipeline

# --- Streamlit App ---

# Set the page title
st.set_page_config(page_title="CircularAgent: Sustainable Material Advisor", page_icon="♻️")

# Title
st.title("♻️ CircularAgent: Sustainable Material Advisor")
st.subheader("Empowering sustainable material decisions through intelligent simulation.")

# User input
user_query = st.text_area(
    "Describe your manufacturing sustainability goal:",
    placeholder="e.g., I want to reduce emissions without increasing costs significantly."
)

# Button to run the agent
if st.button("Analyze"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            final_summary = run_pipeline(user_query)
        st.success("Here's what we found:")
        st.markdown(f"```text\n{final_summary}\n```")
    else:
        st.warning("Please enter a description of your goal.")

# Footer
st.caption("Built for Microsoft AI Agents Hackathon ✨")
