class LCAAgent:
    def __init__(self, goal: str):
        """Initialize the LCA agent with the user's sustainability goal."""
        self.goal = goal.lower()

    def select_impact_factors(self):
        """Agent selects which LCA categories to prioritize based on user intent."""
        if "emission" in self.goal:
            return ["CO2"]
        elif "water" in self.goal:
            return ["Water"]
        else:
            return ["CO2", "Water"]

    def compute_lca(self, simulation_result):
        """Agent computes emissions based on selected LCA impact factors."""
        factors = self.select_impact_factors()
        energy = simulation_result.get("energy_per_kg", 0)
        water = simulation_result.get("water_per_kg", 0)

        total_emissions = 0.0
        if "CO2" in factors:
            total_emissions += 0.4 * energy  # kg CO₂-eq per MJ
        if "Water" in factors:
            total_emissions += 0.0002 * water  # kg CO₂-eq per liter

        return {
            "emissions_per_kg": round(total_emissions, 2),
            "impact_factors": factors
        }