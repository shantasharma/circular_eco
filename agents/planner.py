from agents.utils.together_llm import together_chat_completion

def interpret_user_input(user_text):
    try:
        prompt = f"""
You are an expert in sustainable manufacturing planning.
Given the user's goal, extract the following as a JSON object:
- goal: the sustainability objective
- material: current or suggested material (e.g. PET)
- constraints: any stated constraints
- priority: 'emissions', 'cost', or 'emissions_under_cost_constraint'

User: {user_text}
"""
        raw_output = together_chat_completion(prompt)
        structured = eval(raw_output) if isinstance(raw_output, str) else raw_output

        return {
            "industry": "packaging",
            "process": "bottle_manufacturing",
            "current_material": structured.get("material", "PET"),
            "goal": structured.get("goal", "reduce_footprint"),
            "constraints": structured.get("constraints", []),
            "priority": structured.get("priority", "emissions")
        }
    except Exception as e:
        print("LLM parsing failed, falling back. Reason:", e)
        return {
            "industry": "packaging",
            "process": "bottle_manufacturing",
            "current_material": "PET",
            "goal": "reduce_footprint",
            "constraints": ["no major cost increase"],
            "priority": "emissions_under_cost_constraint"
        }