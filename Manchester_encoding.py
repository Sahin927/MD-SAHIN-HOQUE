import numpy as np
import matplotlib.pyplot as plt

def manchester_encoding(bit_sequence):
    encoded = []
    time = []
    t = 0
    
    for bit in bit_sequence:
        if bit == '1':
            encoded.extend([1, -1])  # '1' → High to Low
        else:
            encoded.extend([-1, 1])  # '0' → Low to High
        
        time.extend([t, t + 0.5])  # Time values for transitions
        t += 1
    
    time.append(t)  # Ensure time and encoded lists match in length
    encoded.append(encoded[-1])  # Extend encoded signal to match time
    print(time)
    print(encoded)
    
    return time, encoded

def plot_manchester_encoding(bit_sequence):
    time, encoded = manchester_encoding(bit_sequence)
    
    plt.figure(figsize=(10, 4))
    plt.step(time, encoded, where='post', color='b', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('Time')
    plt.ylabel('Voltage Level')
    plt.title('Manchester Encoding')
    plt.yticks([-1, 1], ['Low', 'High'])
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Annotate bits
    for i, bit in enumerate(bit_sequence):
        plt.text(i + 0.25, 1.2, bit, fontsize=12, fontweight='bold')

    plt.show()

# Get user input and validate
bit_sequence = input("Enter a binary sequence (e.g., 101010): ")
if not all(bit in '01' for bit in bit_sequence):
    print("Invalid input! Please enter only binary digits (0s and 1s).")
else:
    plot_manchester_encoding(bit_sequence)

