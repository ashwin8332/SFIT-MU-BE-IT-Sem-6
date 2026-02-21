import math

# User-defined inputs
total_channels = int(input("Enter total voice channels: "))
holding_time = float(input("Enter call holding time (sec): "))
gamma = float(input("Enter path loss exponent (gamma): "))
interferers = int(input("Enter number of interferers: "))

cluster_sizes = [4, 7, 12]

for N in cluster_sizes:
    channels_per_cell = total_channels // N

    # Calls per hour per cell
    calls_per_hour = (channels_per_cell * 3600) / holding_time

    # Mean S/I ratio calculation
    DR = math.sqrt(3 * N)
    SI = (DR ** gamma) / interferers
    SI_dB = 10 * math.log10(SI)

    print(f"\nCluster Size (N) = {N}")
    print("Channels per cell:", channels_per_cell)
    print("Calls per cell per hour:", round(calls_per_hour, 2))
    print("Mean S/I ratio (dB):", round(SI_dB, 2))
