import matplotlib.pyplot as plt

def differential_manchester_encode(binary_data):
    """
    Encode binary data using Differential Manchester Encoding.
    
    Convention:
    - For bit '0': A transition occurs at the beginning of the bit period.
    - For bit '1': No transition at the beginning.
    In all cases, a mid-bit transition is always present.
    """
    encoded_signal = []
    last_level = 1
    time = []
    t = 0

    for bit in binary_data:
        time.append(t)
        if bit == '0':
            last_level = 1 - last_level
            encoded_signal.append(last_level)
            time.append(t + 0.5)
            last_level = 1 - last_level
            encoded_signal.append(last_level)
        elif bit == '1':
            encoded_signal.append(last_level)
            time.append(t + 0.5)
            last_level = 1 - last_level
            encoded_signal.append(last_level)
        else:
            raise ValueError("Invalid bit in input: only '0' and '1' are allowed")
        t += 1

    time.append(t)
    encoded_signal.append(last_level)
    
    return time, encoded_signal

def plot_differential_manchester_encoding(bit_sequence):
    time, encoded = differential_manchester_encode(bit_sequence)

    plt.figure(figsize=(10, 4))
    plt.step(time, encoded, where='post', color='b', linewidth=2)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('Time')
    plt.ylabel('Voltage Level')
    plt.title('Differential Manchester Encoding')
    plt.yticks([-1, 1], ['Low', 'High'])
    plt.grid(True, linestyle='--', linewidth=0.5)

    for i, bit in enumerate(bit_sequence):
        plt.text(i + 0.25, 1.2, bit, fontsize=12, fontweight='bold')

    plt.show()

binary_input = input("Enter binary data: ")
if not all(bit in '01' for bit in binary_input):
    print("Invalid input! Only binary digits (0 and 1) are allowed.")
else:
    time_samples, encoded_signal = differential_manchester_encode(binary_input)
    print("Encoded Differential Manchester Signal (time, voltage):")
    print(list(zip(time_samples, encoded_signal)))
    plot_differential_manchester_encoding(binary_input)

