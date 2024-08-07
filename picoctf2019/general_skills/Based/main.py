# Danh sách các chuỗi nhị phân
binary_values = ['01110000', '01100101', '01100001', '01110010']

# Danh sách các chuỗi octal
octal_values = ['156', '165', '162', '163', '145']

# Danh sách các chuỗi hex (đã chia thành các phần nhỏ hơn)
hex_values = ['63', '6f', '6c', '6f', '72', '61', '64', '6f']

# Chuyển đổi từng chuỗi nhị phân thành ký tự
text_binary = "".join([chr(int(binary, 2)) for binary in binary_values])

# Chuyển đổi từng chuỗi octal thành ký tự
text_octal = ''.join(chr(int(oct_value, 8)) for oct_value in octal_values)

# Chuyển đổi từng chuỗi hex thành ký tự
text_hexal = ''.join(chr(int(hex_value, 16)) for hex_value in hex_values)

print("Binary to text:", text_binary)
print("Octal to text:", text_octal)
print("Hex to text:", text_hexal)
