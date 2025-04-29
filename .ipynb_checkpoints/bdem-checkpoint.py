import biosteam as bst

# Define chemicals
from biosteam import Chemical, Chemicals

Water = Chemical('Water')
Glucose = Chemical('Glucose')
chemicals = Chemicals([Water, Glucose])

bst.settings.set_thermo(chemicals)  # Register chemicals

# Define streams
feed = bst.Stream('feed', Water=500, Glucose=100, units='kg/hr')

# Define simple mixer
M1 = bst.units.Mixer('M1', ins=(feed, feed))

# Create system
system = bst.System('simple_system', path=(M1,))

# Simulate
system.simulate()

# Check output
print(M1.outs[0].show())
