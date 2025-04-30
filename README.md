# CircularAgent: Sustainable Material Advisor ♻️

**CircularAgent** is an autonomous agent designed to help manufacturers transition to more sustainable materials.
It evaluates the environmental and economic impact of material alternatives (like switching from PET to rPET),
and recommends the best option based on user goals (e.g., minimize cost, emissions, or both).

## 🔍 Features
- Agentic architecture (Planner, Simulation, Insight Synthesizer, Supplier Matcher)
- Internal simulation engine for PET and rPET production
- Smart reasoning based on user goals (ReAct-style planning)
- Final recommendation backed by comparative analysis
- Streamlit front-end for easy use and demo

## 🚀 Try it locally
```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

## 📊 Example Query
> I want to reduce emissions without increasing cost too much.

**Agent Output:**
- PET vs rPET comparison on cost, energy, CO₂, water
- Recommended material: **rPET**

## 🧠 Architecture Diagram
(*Attach image here if available — Streamlit UI → Planner Agent → Simulation Agent → Insight Synthesizer → Output*)

## 💡 Motivation
Manufacturers are under increasing pressure to meet ESG and sustainability goals. However, the decision to switch materials is complex. CircularAgent automates this reasoning process.

## 📁 Folder Structure
```
circularagent/
├── app.py
├── main.py
├── coordinator.py
├── README.md
├── requirements.txt
├── agents/
│   ├── planner.py
│   ├── simulator.py
│   ├── insight_synthesizer.py
│   └── matcher.py
├── simulators/
│   ├── pet_simulator.py
│   └── rpet_simulator.py
```

---

# === requirements.txt ===
streamlit

# Optional: include only what's actually needed
# pandas
# numpy
# rich
