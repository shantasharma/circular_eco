from agents.utils.together_llm import together_chat_completion

def synthesize_insight(plan, ref_result, alt_results):
    insights = []
    best_material = None
    best_score = None

    for material, result in alt_results.items():
        cost_diff = result['cost_per_kg'] - ref_result['cost_per_kg']
        energy_diff = result['energy_per_kg'] - ref_result['energy_per_kg']
        emissions_diff = result['emissions_per_kg'] - ref_result['emissions_per_kg']
        suppliers = result['suppliers']

        insight = f"Material: {material}\n"
        insight += f"- Cost change: {cost_diff:+.2f}\n"
        insight += f"- Energy change: {energy_diff:+.2f} MJ/kg\n"
        insight += f"- Emissions change: {emissions_diff:+.2f} kg CO2\n"
        insight += f"- Suppliers: {', '.join(suppliers)}\n"
        insights.append(insight)

        # Decision logic
        if plan['priority'] == "cost":
            score = cost_diff
        elif plan['priority'] == "emissions":
            score = emissions_diff
        elif plan['priority'] == "emissions_under_cost_constraint":
            score = emissions_diff if cost_diff <= 0.05 else None
        else:
            score = None

        if score is not None and (best_score is None or score < best_score):
            best_score = score
            best_material = material

    explanation = ""
    try:
        if plan.get("show_reasoning", False):
            prompt = f"Given the sustainability goal '{plan['goal']}', explain why switching from {plan['current_material']} to {best_material} is the best choice."
            explanation = together_chat_completion(prompt)
    except Exception as e:
        explanation = "LLM explanation unavailable."

    summary = "\n=== Material Alternatives Summary ===\n" + "\n".join(insights)
    if best_material:
        summary += f"\n\n✅ Recommended Material: {best_material}\nReason: Best fit for '{plan['priority']}' objective."
        if plan.get("show_reasoning"):
            summary += f"\n\n💬 LLM Justification:\n{explanation}"
    else:
        summary += "\n\n⚠️ No material meets the constraints."

    return summary