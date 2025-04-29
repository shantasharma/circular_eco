# === coordinator.py ===

from agents.planner import interpret_user_input
from agents.simulator import simulate_process
from agents.lca_agent import estimate_emissions
from agents.matcher import get_suppliers
from agents.insight_synthesizer import synthesize_insight

def run_pipeline(user_query):
    plan = interpret_user_input(user_query)

    ref_material = plan['current_material']
    alt_materials = ["rPET"]

    ref_result = simulate_process(ref_material)
    ref_result['emissions'] = estimate_emissions(ref_material)

    alt_results = {}
    for alt in alt_materials:
        alt_result = simulate_process(alt)
        alt_result['emissions'] = estimate_emissions(alt)
        alt_result['suppliers'] = get_suppliers(alt)
        alt_results[alt] = alt_result

    final_summary = synthesize_insight(plan, ref_result, alt_results)
    return final_summary
