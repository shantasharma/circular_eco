class PETSimulator:
    @staticmethod
    def simulate():
        """Simulates PET production process."""
        return {
            "cost_per_kg": 1.10,         # USD per kg PET
            "energy_per_kg": 5.2,         # MJ per kg PET
            "water_per_kg": 2.5,          # Liters per kg PET
            "emissions_per_kg": 2.8       # kg CO2 equivalent per kg PET
        }