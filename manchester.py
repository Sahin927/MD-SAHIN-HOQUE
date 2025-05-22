import matplotlib.pyplot as plt

def nrzi_encode(data):
    result = []
    last = 1  # Start high (1)
    for bit in data:
        if bit == '1':
            last ^= 1  # Toggle signal
        result.append(last)
    return result

def manchester_encode(data):
    result = []
    for bit in data:
        if bit == '0':
            result += [1, 0]  # high to low
        else:
            result += [0, 1]  # low to high
    return result

def differential_manchester_encode(data):
    result = []
    last = 1  # Start high (1)
    for bit in data:
        if bit == '0':
            last ^= 1  # extra transition
        result.append(last)
        last ^= 1  # mid-bit transition always
        result.append(last)
    return result

def plot_signal(data, title, bits_per_symbol=1):
    time = []
    voltage = []

    for i, bit in enumerate(data):
        t = i / bits_per_symbol
        time.extend([t, t + 1 / bits_per_symbol])
        voltage.extend([bit, bit])

    plt.figure(figsize=(10, 2))
    plt.step(time, voltage, where='post')
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1])
    plt.title(title)
    plt.grid(True)
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.show()

# ----------- MAIN ------------
binary = input("Enter binary input (e.g., 1011001): ").strip()

nrzi = nrzi_encode(binary)
manchester = manchester_encode(binary)
diff_manchester = differential_manchester_encode(binary)

print("\nEncoded outputs:")
print("NRZI:              ", ''.join(map(str, nrzi)))
print("Manchester:        ", ''.join(map(str, manchester)))
print("Diff. Manchester:  ", ''.join(map(str, diff_manchester)))

plot_signal(nrzi, "NRZI Encoding")
plot_signal(manchester, "Manchester Encoding", bits_per_symbol=2)
plot_signal(diff_manchester, "Differential Manchester Encoding", bits_per_symbol=2)

