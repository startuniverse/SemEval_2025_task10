from openai import OpenAI
import os
import json


client = OpenAI(
    base_url='API',  
    api_key='SK-XXX'  
)


prompt = "You can only output the option words I provided, and you are not allowed to generate any other options. Do not generate any explanatory or descriptive text."


input_folder = "/root/autodl-tmp/ai/test/PT/subtask-1-documents"
output_file = "/root/autodl-tmp/ai/test/output/S1PT4o.txt"
json_file = "/root/autodl-tmp/ai/test/TESTS1PT.json"



try:
    with open(json_file, "r", encoding="utf-8") as f:
        ne_data = json.load(f)
except Exception as e:
    print(f"error: {e}")
    exit()


with open(output_file, "w", encoding="utf-8") as f_out:

    for entry in ne_data:
        filename = entry["filename"]
        ne = entry.get("NE", "")
        start = entry.get("start", "")
        end = entry.get("end", "")

        print(f"\n{filename}")


        txt_path = os.path.join(input_folder, filename)


        if not os.path.exists(txt_path):
            print(f" error: {txt_path}")
            f_out.write(f"filename: {filename}\n")
            f_out.write("-" * 50 + "\n")
            continue

        try:
         
            with open(txt_path, "r", encoding="utf-8") as f_in:
                article = f_in.read().replace("\n", " ")

           
            messages = [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user",
                 "content": "I will provide you with a news article and a person's name. This person's name will appear in the article. Please identify what kind of role this person's name belongs to based on the content of the article. You have three options: Protagonist, Antagonist, Innocent." + prompt},
                {"role": "assistant", "content": "Sure! Please provide me with the news article."},
                {"role": "user",
                 "content": f"news article:{article}\nThe article is over. The person's name you need to process is: [{ne}]"},
            ]

           
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=500,  
                temperature=0.0,  
            )
            generated_text = completion.choices[0].message.content.strip() 
            print(f"result: {generated_text}")

          
            f_out.write(f"{filename}\t")
            f_out.write(f"{ne}\t")
            f_out.write(f"{start}\t")
            f_out.write(f"{end}\t")
            f_out.write(f"{generated_text}\t")

     
            if "Protagonist" in generated_text:
            
                messages.append({"role": "user",
                                 "content": 'Under this role, there is a more detailed classification task. Please select a more specific role for this person according to the news article. You have the following options:Guardian,Martyr,Peacemaker,Rebel,Underdog,Virtuous.' + prompt})
          
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.0,
                )
                subcategory_result = completion.choices[0].message.content.strip()
                f_out.write(f"{subcategory_result}\n")

            elif "Antagonist" in generated_text:

                messages.append({"role": "user",
                                 "content": 'Under this role, there is a more detailed classification task. Please select a more specific role for this person according to the news article. You have the following options:Instigator,Conspirator,Tyrant,Foreign Adversary,Traitor,Spy,Saboteur,Corrupt,Incompetent,Terrorist,Deceiver,Bigot.' + prompt})
          
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.0,
                )
                subcategory_result = completion.choices[0].message.content.strip()
                f_out.write(f"{subcategory_result}\n")

            elif "Innocent" in generated_text:
         
                messages.append({"role": "user",
                                 "content": 'Under this role, there is a more detailed classification task. Please select a more specific role for this person according to the news article. You have the following options:Forgotten,Exploited,Victim,Scapegoat.' + prompt})

                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500,
                    temperature=0.0,
                )
                subcategory_result = completion.choices[0].message.content.strip()
                f_out.write(f"{subcategory_result}\n")

print(f"save in: {output_file}")
