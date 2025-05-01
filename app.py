# === app.py ===

import streamlit as st
from coordinator import run_pipeline
from agents.planner import interpret_user_input

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

# Priority selector
st.markdown("## 🎯 Set Your Optimization Priority")
selected_priority = st.radio(
    "Choose the most important sustainability goal:",
    ["Minimize Emissions", "Minimize Cost", "Balance Emissions and Cost"],
    index=0
)

priority_map = {
    "Minimize Emissions": "emissions",
    "Minimize Cost": "cost",
    "Balance Emissions and Cost": "emissions_under_cost_constraint"
}

# Reasoning checkbox
show_reasoning = st.checkbox("🔎 Show agent reasoning behind recommendation")

# Run button
if st.button("Analyze"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            plan = interpret_user_input(user_query)
            plan["priority"] = priority_map[selected_priority]
            plan["show_reasoning"] = show_reasoning
            final_summary = run_pipeline(plan)  # Pass full plan instead of raw query
        st.success("Here's what we found:")
        st.markdown(f"```text\n{final_summary}\n```")
    else:
        st.warning("Please enter a description of your goal.")

# Footer
st.caption("Built for Microsoft AI Agents Hackathon ✨")
