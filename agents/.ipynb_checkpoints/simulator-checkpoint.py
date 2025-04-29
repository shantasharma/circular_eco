from simulators.pet_simulator import PETSimulator
from simulators.rpet_simulator import RPETSimulator

material_simulators = {
    "PET": PETSimulator,
    "rPET": RPETSimulator,
}

def simulate_process(material):
    simulator = material_simulators.get(material)
    if simulator:
        return simulator.simulate()
    else:
        raise ValueError(f"Unknown material: {material}")