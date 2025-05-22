import random

def binary_addition(a, b):
    result = ''
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        result = str(total % 2) + result
        carry = total // 2
    if carry:
        result = '1' + result
    return result[-len(a):]

def ones_complement(binary):
    return ''.join('1' if bit == '0' else '0' for bit in binary)

def compute_checksum(data, section_size):
    sections = [data[i:i+section_size] for i in range(0, len(data), section_size)]
    if len(sections[-1]) < section_size:
        sections[-1] = sections[-1].ljust(section_size, '0')

    checksum = sections[0]
    for section in sections[1:]:
        checksum = binary_addition(checksum, section)
    return ones_complement(checksum)

def verify_checksum(data, checksum, section_size):
    total = binary_addition(data[:len(checksum)], checksum)
    return all(bit == '1' for bit in total)

# CRC Functions
def xor(a, b):
    return ''.join(['0' if i == j else '1' for i, j in zip(a, b)])

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
        tmp = tmp.lstrip('0').rjust(len(divisor)-1, '0')
    return xor(divisor, tmp) if tmp[0] == '1' else tmp

def compute_crc(data, poly):
    padded_data = data + '0' * (len(poly) - 1)
    remainder = mod2div(padded_data, poly)
    return remainder

def verify_crc(data_with_crc, poly):
    remainder = mod2div(data_with_crc, poly)
    return int(remainder) == 0

# --- MAIN ---
data = input("Enter binary data: ").strip()

# ----- CHECKSUM -----
print("\n--- Checksum Calculation ---")
section_size = int(input("Enter section size (e.g., 8): "))
checksum = compute_checksum(data, section_size)
transmitted_data = data + checksum
print("Checksum:             ", checksum)
print("Transmitted Data:     ", transmitted_data)

# Simulate error
error_pos = random.randint(0, len(transmitted_data)-1)
corrupted_data = list(transmitted_data)
corrupted_data[error_pos] = '1' if corrupted_data[error_pos] == '0' else '0'
corrupted_data = ''.join(corrupted_data)

print("Corrupted Data:       ", corrupted_data)
if verify_checksum(corrupted_data, checksum, section_size):
    print("Result: No error detected.")
else:
    print("Result: Error detected!")

# ----- CRC -----
print("\n--- CRC Calculation ---")
poly = input("Enter generator polynomial (e.g., 1101): ").strip()
crc = compute_crc(data, poly)
data_with_crc = data + crc
print("CRC:                  ", crc)
print("Transmitted Data:     ", data_with_crc)

# Simulate error
crc_corrupted = list(data_with_crc)
error_pos = random.randint(0, len(crc_corrupted)-1)
crc_corrupted[error_pos] = '1' if crc_corrupted[error_pos] == '0' else '0'
crc_corrupted = ''.join(crc_corrupted)

print("Corrupted Data:       ", crc_corrupted)
if verify_crc(crc_corrupted, poly):
    print("Result: No error detected.")
else:
    print("Result: Error detected!")



