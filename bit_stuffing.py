def get_consecutive_ones_in_flag(flag):
    max_count = 0
    count = 0
    for bit in flag:
        if bit == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

def bit_stuff(data, threshold):
    stuffed = ''
    count = 0
    for bit in data:
        stuffed += bit
        if bit == '1':
            count += 1
            if count == threshold:
                stuffed += '0'  # Stuff a '0' after threshold 1's
                count = 0
        else:
            count = 0
    return stuffed

def bit_unstuff(stuffed, threshold):
    unstuffed = ''
    count = 0
    i = 0
    while i < len(stuffed):
        bit = stuffed[i]
        unstuffed += bit
        if bit == '1':
            count += 1
            if count == threshold:
                i += 1  # Skip the stuffed '0'
                count = 0
        else:
            count = 0
        i += 1
    return unstuffed

# ------------ MAIN ------------
data = input("Enter binary data: ").strip()
flag = input("Enter flag pattern (e.g., 11110): ").strip()

# Step 1: Count max consecutive 1s in flag
n_consecutive_1s = get_consecutive_ones_in_flag(flag)
# Step 2: Bit stuffing threshold = n - 1
stuffing_threshold = n_consecutive_1s - 1 if n_consecutive_1s > 1 else 1

stuffed_data = bit_stuff(data, stuffing_threshold)
transmitted = flag + stuffed_data + flag
received_data = transmitted[len(flag):-len(flag)]
unstuffed_data = bit_unstuff(received_data, stuffing_threshold)

print("\n--- Bit Stuffing ---")
print("Original Data:     ", data)
print("Flag Pattern:      ", flag)
print("Stuffing After:    ", stuffing_threshold, "consecutive 1's")
print("Stuffed Data:      ", stuffed_data)
print("Transmitted Frame: ", transmitted)
print("Received Data:     ", received_data)
print("De-stuffed Data:   ", unstuffed_data)



