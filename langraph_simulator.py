class SimulationStep:
    def __init__(self, material_data):
        self.data = material_data

    def run(self):
        return {
            "cost_per_kg": self.data["cost_per_kg"],
            "energy_per_kg": self.data["energy_per_kg"],
            "water_per_kg": self.data["water_per_kg"]
        }