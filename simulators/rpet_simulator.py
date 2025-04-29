class RPETSimulator:
    @staticmethod
    def simulate():
        """Simulates rPET recycling process."""
        return {
            "cost_per_kg": 1.00,         # USD per kg rPET
            "energy_per_kg": 3.0,         # MJ per kg rPET
            "water_per_kg": 1.2,          # Liters per kg rPET
            "emissions_per_kg": 1.6       # kg CO2 equivalent per kg rPET
        }
