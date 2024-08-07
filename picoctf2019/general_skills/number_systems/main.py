def convert_to_text(number_list, base):
    if base == 'binary':
        # Chuyển đổi từ nhị phân thành ký tự
        text = ''.join(chr(int(binary, 2)) for binary in number_list)
    elif base == 'octal':
        # Chuyển đổi từ octal thành ký tự
        text = ''.join(chr(int(octal, 8)) for octal in number_list)
    elif base == 'hex':
        # Chuyển đổi từ hex thành ký tự
        text = ''.join(chr(int(hex_value, 16)) for hex_value in number_list)
    elif base == 'decimal':
        # Chuyển đổi từ decimal thành ký tự
        text = ''.join(chr(num) for num in number_list)
    elif base == 'ascii':
        # Chuyển đổi từ ASCII mã số thành ký tự
        text = ''.join(chr(num) for num in number_list)
    else:
        raise ValueError("Unsupported base")
    
    return text

def get_input_for_base(base):
    if base == 'binary':
        return input("Enter a list of binary numbers separated by commas (e.g., 01110000, 01100101): ")
    elif base == 'octal':
        return input("Enter a list of octal numbers separated by commas (e.g., 156, 165): ")
    elif base == 'hex':
        return input("Enter a list of hexadecimal numbers separated by commas (e.g., 70, 65): ")
    elif base == 'decimal':
        return input("Enter a list of decimal numbers separated by commas (e.g., 112, 101): ")
    elif base == 'ascii':
        return input("Enter a list of ASCII codes separated by commas (e.g., 112, 101): ")
    else:
        raise ValueError("Unsupported base")

def main():
    try:
        base = input("Enter the base (binary, octal, hex, decimal, ascii): ").strip().lower()
        user_input = get_input_for_base(base)
        
        # Chuyển đổi chuỗi nhập vào thành danh sách số nguyên
        if base in ['binary', 'octal', 'hex']:
            number_list = [num.strip() for num in user_input.split(',')]
        else:
            number_list = [int(num.strip()) for num in user_input.split(',')]
        
        # Chuyển đổi và in kết quả
        text = convert_to_text(number_list, base)
        print(f"{base.capitalize()} to Text: {text}")
        
    except ValueError as e:
        print(f"Invalid input! {e}")

# Chạy chương trình chính
if __name__ == "__main__":
    main()
