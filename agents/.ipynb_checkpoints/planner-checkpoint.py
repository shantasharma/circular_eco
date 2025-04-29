def interpret_user_input(user_text):
    plan = {
        "industry": "packaging",
        "process": "bottle_manufacturing",
        "current_material": "PET",
        "goal": "reduce_footprint",
        "constraints": [],
        "priority": "emissions"  # default
    }

    lower_text = user_text.lower()

    # Detect material if explicitly mentioned
    if "bottle" in lower_text:
        plan["current_material"] = "PET"

    # Detect primary optimization goal
    if "cost" in lower_text and "emission" not in lower_text:
        plan["priority"] = "cost"
    elif "emission" in lower_text and "cost" not in lower_text:
        plan["priority"] = "emissions"
    elif "cost" in lower_text and "emission" in lower_text:
        plan["priority"] = "emissions_under_cost_constraint"
        plan["constraints"].append("no major cost increase (e.g., <5%)")

    return plan