ascii_values = [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]

characters = [chr(value)for value in ascii_values]

message = ''.join(characters)

print(message)