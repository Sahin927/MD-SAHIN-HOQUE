import matplotlib.pyplot as plt

def nrz_i_encoding(bit_sequence):
    encoded = []  # Stores the encoded signal (voltage levels)
    time = []     # Stores the time points
    t = 0         # Time tracker
    current_level = 1  # Assume initial level is HIGH (1)

    for bit in bit_sequence:
        if bit == '1':
            current_level *= -1  # Flip the signal
        encoded.append(current_level)  # Append current voltage level
        time.append(t)  # Append time step
        t += 1  # Move to the next time step

    # Extend time and encoded list to match length
    time.append(t)
    encoded.append(encoded[-1])

    return time, encoded

# Get user input
bit_sequence = input("Enter a binary sequence (0s and 1s): ")

# Validate input
if not all(bit in '01' for bit in bit_sequence):
    print("Invalid input! Please enter only binary digits (0s and 1s).")
else:
    # Encode using NRZ-I
    time, encoded = nrz_i_encoding(bit_sequence)

    # Plot NRZ-I Signal
    plt.figure(figsize=(10, 4))
    plt.step(time, encoded, where='post', color='b', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('Time')
    plt.ylabel('Voltage Level')
    plt.title('NRZ-I Encoding')
    plt.yticks([-1, 1], ['Low', 'High'])
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Annotate the bits on top of the graph
    for i, bit in enumerate(bit_sequence):
        plt.text(i + 0.25, 1.2, bit, fontsize=12, fontweight='bold')

    plt.show()

