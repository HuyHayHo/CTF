# Danh sách các chuỗi nhị phân
binary_values = ['01101100', '01101001', '01100111', '01101000', '01110100', '01110100']

# Danh sách các chuỗi octal
octal_values = ['143', '157', '156', '164', '141', '151', '145', '162']

# Danh sách các chuỗi hex (đã chia thành các phần nhỏ hơn)
hex_values = ['70','69','65']

# Chuyển đổi từng chuỗi nhị phân thành ký tự
text_binary = "".join([chr(int(binary, 2)) for binary in binary_values])

# Chuyển đổi từng chuỗi octal thành ký tự
text_octal = ''.join(chr(int(oct_value, 8)) for oct_value in octal_values)

# Chuyển đổi từng chuỗi hex thành ký tự
text_hexal = ''.join(chr(int(hex_value, 16)) for hex_value in hex_values)

print("Binary to text:", text_binary)
print("Octal to text:", text_octal)
print("Hex to text:", text_hexal)
