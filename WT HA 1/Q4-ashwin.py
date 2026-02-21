# Given values
total_area = 4200        # km^2
cell_area = 12           # km^2
total_channels = 1001

# Calculate number of cells
num_cells = total_area / cell_area
print("Number of cells =", int(num_cells))

# Case (a)
N = 7
clusters = num_cells / N
channels_per_cell = total_channels / N
system_capacity = channels_per_cell * num_cells
print("\nCase (a):")
print("Cluster size =", N)
print("Number of clusters =", int(clusters))
print("Channels per cell =", int(channels_per_cell))
print("System capacity =", int(system_capacity), "channels")

# Case (b)
N = 4
cluster = num_cells / N
channels_per_cell = total_channels / N
system_capacity = channels_per_cell * num_cells
print("\nCase (b):")
print("Cluster size =", N)
print("Number of clusters =", int(cluster))
print("Channels per cell =", int(channels_per_cell))
print("System capacity =", int(system_capacity), "channels")
