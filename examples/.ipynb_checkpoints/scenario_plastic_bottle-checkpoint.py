import sys

sys.path.append("/projects/illinois/ovcri/ncsa/blatti/omics_chat/oneIE/circular")

from agents.planner import interpret_user_input
from agents.simulator import simulate_process
from agents.lca_agent import estimate_emissions
from agents.matcher import get_suppliers

query = "Can I switch from PET bottle to recycled plastic without increasing cost?"
plan = interpret_user_input(query)

alt_materials = ["rPET", "bioPET"]
print(f"\nCurrent material: {plan['current_material']}")
ref = simulate_process(plan['current_material'])

for alt in alt_materials:
    result = simulate_process(alt)
    cost_diff = result['cost'] - ref['cost']
    energy_diff = result['energy'] - ref['energy']
    emission = estimate_emissions(alt)
    print(f"\nAlternative: {alt}")
    print(f"  Cost change: {cost_diff:.2f}")
    print(f"  Energy change: {energy_diff:.2f} MJ/kg")
    print(f"  Estimated CO2: {emission:.2f} kg")
    print(f"  Suppliers: {', '.join(get_suppliers(alt))}")