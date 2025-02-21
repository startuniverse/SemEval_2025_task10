from openai import OpenAI
import os
import json

# 设置 OpenAI 客户端
client = OpenAI(
    base_url='API',  # 替换为你的 API 地址
    api_key='SK-XXX'  # 替换为你的 OpenAI API Key
)

# 定义提示词
prompt = "You can only output the option words I provided, and you are not allowed to generate any other options. Do not generate any explanatory or descriptive text."

# 路径配置
input_folder = "/root/autodl-tmp/ai/test/PT/subtask-1-documents"
output_file = "/root/autodl-tmp/ai/test/output/S1PT4o.txt"
json_file = "/root/autodl-tmp/ai/test/TESTS1PT.json"

# 检查输入文件
if not all([os.path.exists(input_folder), os.path.exists(json_file)]):
    print("输入文件缺失")
    exit()

# 加载NE数据
try:
    with open(json_file, "r", encoding="utf-8") as f:
        ne_data = json.load(f)
except Exception as e:
    print(f"加载JSON文件失败: {e}")
    exit()

# 打开输出文件，准备写入结果
with open(output_file, "w", encoding="utf-8") as f_out:
    # 遍历JSON中的每个条目
    for entry in ne_data:
        filename = entry["filename"]
        ne = entry.get("NE", "")
        start = entry.get("start", "")
        end = entry.get("end", "")

        print(f"\n正在处理条目: {filename}")

        # 构建完整文件路径
        txt_path = os.path.join(input_folder, filename)

        # 检查TXT文件是否存在
        if not os.path.exists(txt_path):
            print(f" ! 文件不存在: {txt_path}")
            f_out.write(f"文件名: {filename}\n")
            f_out.write(f"错误: 对应TXT文件不存在\n")
            f_out.write("-" * 50 + "\n")
            continue

        try:
            # 读取文章内容
            with open(txt_path, "r", encoding="utf-8") as f_in:
                article = f_in.read().replace("\n", " ")

            # 构建消息
            messages = [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user",
                 "content": "I will provide you with a news article and a person's name. This person's name will appear in the article. Please identify what kind of role this person's name belongs to based on the content of the article. You have three options: Protagonist, Antagonist, Innocent." + prompt},
                {"role": "assistant", "content": "Sure! Please provide me with the news article."},
                {"role": "user",
                 "content": f"news article:{article}\nThe article is over. The person's name you need to process is: [{ne}]"},
            ]

            # 调用 OpenAI API 生成文本
            completion = client.chat.completions.create(
                model="gpt-4o",  # 使用 GPT-4 模型
                messages=messages,
                max_tokens=500,  # 最大生成 token 数
                temperature=0.0,  # 控制生成文本的随机性
            )
            generated_text = completion.choices[0].message.content.strip()  # 获取生成的文本并去除首尾空格
            print(f"生成结果: {generated_text}")

            # 写入基础结果
            f_out.write(f"{filename}\t")
            f_out.write(f"{ne}\t")
            f_out.write(f"{start}\t")
            f_out.write(f"{end}\t")
            f_out.write(f"{generated_text}\t")

            # 检测生成的文本是否包含 Protagonist、Antagonist 或 Innocent
            if "Protagonist" in generated_text:
                print("检测到 Protagonist，继续提问子分类。")
                # 添加子分类问题
                messages.append({"role": "user",
                                 "content": 'Under this role, there is a more detailed classification task. Please select a more specific role for this person according to the news article. You have the following options:Guardian,Martyr,Peacemaker,Rebel,Underdog,Virtuous.' + prompt})
                # 生成子分类回答
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.0,
                )
                subcategory_result = completion.choices[0].message.content.strip()
                print(f"子分类结果: {subcategory_result}")
                f_out.write(f"{subcategory_result}\n")

            elif "Antagonist" in generated_text:
                print("检测到 Antagonist，继续提问子分类。")
                # 添加子分类问题
                messages.append({"role": "user",
                                 "content": 'Under this role, there is a more detailed classification task. Please select a more specific role for this person according to the news article. You have the following options:Instigator,Conspirator,Tyrant,Foreign Adversary,Traitor,Spy,Saboteur,Corrupt,Incompetent,Terrorist,Deceiver,Bigot.' + prompt})
                # 生成子分类回答
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.0,
                )
                subcategory_result = completion.choices[0].message.content.strip()
                print(f"子分类结果: {subcategory_result}")
                f_out.write(f"{subcategory_result}\n")

            elif "Innocent" in generated_text:
                print("检测到 Innocent，继续提问子分类。")
                # 添加子分类问题
                messages.append({"role": "user",
                                 "content": 'Under this role, there is a more detailed classification task. Please select a more specific role for this person according to the news article. You have the following options:Forgotten,Exploited,Victim,Scapegoat.' + prompt})
                # 生成子分类回答
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.0,
                )
                subcategory_result = completion.choices[0].message.content.strip()
                print(f"子分类结果: {subcategory_result}")
                f_out.write(f"{subcategory_result}\n")

        except Exception as e:
            print(f"处理失败: {e}")
            f_out.write(f"文件名: {filename}\n")
            f_out.write(f"错误: {str(e)}\n")
            f_out.write("-" * 50 + "\n")

print(f"所有条目处理完成，结果已保存到: {output_file}")