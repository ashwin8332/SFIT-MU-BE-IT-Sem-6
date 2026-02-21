total_spectrum_mhz = 25   # Given total RF spectrum in MHz
channel_bandwidth_khz = 25  # Given channel bandwidth in kHz
# Calculate total number of voice channels supported by the system
total_channels = (total_spectrum_mhz * 1000) / channel_bandwidth_khz
print("Total available voice channels =", int(total_channels))

# Case (a) 
cells = 20  # Service area divided into 20 cells
reuse_factor = 4  # Frequency reuse factor
# Calculate number of channels per cell
channels_per_cell = total_channels / reuse_factor
# Calculate total system capacity
system_capacity = channels_per_cell * cells
print("\nCase (a):")
print("Number of cells =", cells)
print("Reuse factor =", reuse_factor)
print("Channels per cell =", channels_per_cell)
print("System capacity =", int(system_capacity), "channels")

# Case (b)
cells = 100   # Service area divided into 100 cells
reuse_factor = 4  # Frequency reuse factor remains same
# Calculate number of channels per cell
channels_per_cell = total_channels / reuse_factor
# Calculate total system capacity
system_capacity = channels_per_cell * cells
print("\nCase (b):")
print("Number of cells =", cells)
print("Reuse factor =", reuse_factor)
print("Channels per cell =",  channels_per_cell)
print("System capacity =", int(system_capacity), "channels")

# Case (c)
cells = 700   # Service area divided into 700 cells
reuse_factor = 7   # Frequency reuse factor increased to 7
# Calculate number of channels per cell
channels_per_cell = total_channels / reuse_factor
# Calculate total system capacity
system_capacity = channels_per_cell * cells
print("\nCase (c):")
print("Number of cells =", cells)
print("Reuse factor =", reuse_factor)
print("Channels per cell =", channels_per_cell)
print("System capacity =", int(system_capacity), "channels")
