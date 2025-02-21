import os
import json


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def convert_to_json(lines):
    json_list = []

    for line in lines:
        parts = line.strip().split('\t')
        description=[]
        if len(parts) == 4:
            filename=parts[0]
            NE=parts[1]
            start=parts[2]
            end=parts[3]
            json_obj = {
                "filename": filename,
                "NE": NE,
                "start": int(start),
                "end": int(end),
            }
            json_list.append(json_obj)

    return json_list

def save_json(json_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)

# 文件路径
input_file_path = r"D:\zhuomian\test\PT\subtask-1-entity-mentions.txt"
output_file_path = 'TESTS1PT.json'

# 读取文件
lines = read_file(input_file_path)

# 转换为 JSON 格式
json_result = convert_to_json(lines)

# 保存为 JSON 文件
save_json(json_result, output_file_path)

print(f"转换完成！JSON 文件已保存到 {output_file_path}")
