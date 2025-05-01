# === coordinator.py (Updated to receive full plan from Streamlit) ===

from agents.simulator import simulate_process
from agents.lca_agent import LCAAgent
from agents.matcher import get_suppliers
from agents.insight_synthesizer import synthesize_insight

# Updated to accept plan directly from app.py

def run_pipeline(plan):
    ref_material = plan['current_material']
    alt_materials = ["rPET"]

    # Simulate reference material
    ref_result = simulate_process(ref_material)
    lca_agent = LCAAgent(plan['goal'])
    ref_result.update(lca_agent.compute_lca(ref_result))

    # Simulate alternatives
    alt_results = {}
    for alt in alt_materials:
        alt_result = simulate_process(alt)
        alt_result.update(lca_agent.compute_lca(alt_result))
        alt_result['suppliers'] = get_suppliers(alt)
        alt_results[alt] = alt_result

    # Pass full plan to synthesize_insight (includes show_reasoning toggle)
    final_summary = synthesize_insight(plan, ref_result, alt_results)
    return final_summary
