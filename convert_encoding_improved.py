import os
import chardet

def convert_to_utf8(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        if encoding and encoding.lower() != 'utf-8':
            try:
                text = raw_data.decode(encoding)
                with open(file_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(text)
                print(f"Converted {file_path} from {encoding} to UTF - 8")
            except Exception as e:
                print(f"Error converting {file_path}: {e}")

def convert_directory(directory):
    for root, dirs, files in os.walk(directory):
        # 跳过 .git 目录
        if '.git' in root:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            convert_to_utf8(file_path)

project_directory = 'C:/Users/DELL/Desktop/2025年会'
convert_directory(project_directory)