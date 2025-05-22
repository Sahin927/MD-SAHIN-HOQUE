def get_class_bitwise(ip_address):
    octets = ip_address.split(".")
    first_octet = int(octets[0])

    if first_octet == 0:
        return "Special Address (0.0.0.0 – Reserved)"
    elif first_octet == 127:
        return "Loopback Address (127.0.0.0 – 127.255.255.255)"
    elif 1 <= first_octet <= 126:
        return "Class A"
    elif 127 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    else:
        return "Class E (Reserved)"


def get_class_decimal(ip_address):
    return get_class_bitwise(ip_address)


def validate_ip(input_ip, input_format):
    if input_format == "binary":
        try:
            binary_octets = input_ip.split(".")
            if len(binary_octets) != 4 or any(len(octet) != 8 for octet in binary_octets):
                return "Invalid binary IP address format"
            decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
            return ".".join(decimal_octets)
        except ValueError:
            return "Invalid binary IP address"
    elif input_format == "decimal":
        parts = input_ip.split(".")
        if len(parts) != 4 or any(not p.isdigit() or not (0 <= int(p) <= 255) for p in parts):
            return "Invalid decimal IP address"
        return input_ip
    else:
        return "Invalid format"


print("=== IP Class Detection ===")
input_format = input("Enter the format of your IP (binary/decimal): ").strip().lower()

if input_format not in ["binary", "decimal"]:
    print("Invalid input format!")
else:
    ip_address = input("Enter IP address: ").strip()
    validated_ip = validate_ip(ip_address, input_format)

    if validated_ip.startswith("Invalid"):
        print(validated_ip)
    else:
        print(f"\nYour IP address (Decimal Format): {validated_ip}")
        print("IP Class (Bitwise approach):", get_class_bitwise(validated_ip))
        print("IP Class (Decimal approach):", get_class_decimal(validated_ip))

