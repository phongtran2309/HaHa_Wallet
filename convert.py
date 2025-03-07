import json

def convert_file(input_file, output_file):
    try:
        # Đọc nội dung tệp
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Chuyển đổi từng dòng thành đối tượng JSON
        result = []
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                email, password = parts
                result.append({"Email": email.strip(), "Password": password.strip()})
        
        # Ghi kết quả vào tệp JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        
        print(f'Đã chuyển đổi thành công và lưu tại {output_file}')
    except Exception as e:
        print(f'Đã xảy ra lỗi: {e}')

# Gọi hàm với tên tệp đầu vào và đầu ra
convert_file('data.txt', 'accounts.json')
