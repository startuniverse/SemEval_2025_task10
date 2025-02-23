from openai import OpenAI
import os


client = OpenAI(
    base_url='API',  
    api_key='SK-XXX'  
)


prompt = "You should choose one or more options, but only select from the options I have provided. Do not generate any descriptions or explanations."

input_folder = "/root/autodl-tmp/ai/test/PT/subtask-2-documents"
output_file = "/root/autodl-tmp/ai/test/output/S2PT4o.txt" 




with open(output_file, "w", encoding="utf-8") as f_out:
   
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            print(f"{filename}")

            with open(file_path, "r", encoding="utf-8") as f_in:
                article = f_in.read().replace("\n", " ")


            messages = [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": "I want you to complete a narrative classification task. I will give you a news article. After you read the article, you have two options, 'Ukraine War' and 'Climate Change'. If you think the article is related to 'Ukraine War', output 'URW'. If you think the article is related to 'Climate Change', output 'CC'. Your output result should be only 'URW' or 'CC'."},
                {"role": "assistant", "content": "Sure! Please provide me with the news article."},
                {"role": "user", "content": "news article:" + article},
            ]


            try:
                completion = client.chat.completions.create(
                    model="gpt-4o", 
                    messages=messages,
                    max_tokens=500, 
                    temperature=0.0, 
                )
                generated_text = completion.choices[0].message.content.strip() 
 
                f_out.write(f"\n{filename}\t")
                generated_text = generated_text.replace('\n', '')
                f_out.write(f"{generated_text}: ")


                if "URW" in generated_text:

                    messages.append({"role": "user", "content": 'There are subcategories under "URW". Please select the appropriate subcategory that is relevant to the article. The subcategories are as follows: [Other][Blaming the war on others rather than the invader][Discrediting Ukraine][Russia is the Victim][Praise of Russia][Overpraising the West][Speculating war outcomes][Discrediting the West, Diplomacy][Negative Consequences for the West][Distrust towards Media][Amplifying war-related fears][Hidden plots by secret schemes of powerful groups].' + prompt})
        
                    completion = client.chat.completions.create(
                        model="gpt-4o",
                        messages=messages,
                        max_tokens=500,
                        temperature=0.0,
                    )
                    subcategory_result = completion.choices[0].message.content.strip()

                    subcategory_result = subcategory_result.replace('\n', '')
                    subcategory_result = subcategory_result.replace('[', '')
                    subcategory_result = subcategory_result.replace(']', ';')
                    f_out.write(f"{subcategory_result}\t")

                    if "Blaming the war on others rather than the invader" in subcategory_result:

                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Blaming the war on others rather than the invader." The following are more detailed classification options: [Ukraine is the aggressor][The West are the aggressors].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()

                        detailed_result = detailed_result.replace('\n', '')

                        detailed_result = detailed_result.replace('[', '')
       
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Discrediting Ukraine" in subcategory_result:

                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Discrediting Ukraine." The following are more detailed classification options: [Rewriting Ukraine’s history][Discrediting Ukrainian nation and society][Discrediting Ukrainian military][Discrediting Ukrainian government and officials and policies][Ukraine is a puppet of the West][Ukraine is a hub for criminal activities][Ukraine is associated with nazism][Situation in Ukraine is hopeless].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()

                        detailed_result = detailed_result.replace('\n', '')

                        detailed_result = detailed_result.replace('[', '')

                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Russia is the Victim" in subcategory_result:

                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Russia is the Victim." The following are more detailed classification options: [The West is russophobic][Russia actions in Ukraine are only self-defence][UA is anti-RU extremists].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()

                        detailed_result = detailed_result.replace('\n', '')
   
                        detailed_result = detailed_result.replace('[', '')
                   
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Praise of Russia" in subcategory_result:
                   
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Praise of Russia." The following are more detailed classification options: [Praise of Russian military might][Praise of Russian President Vladimir Putin][Russia is a guarantor of peace and prosperity][Russia has international support from a number of countries and people][Russian invasion has strong national support].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                  
                        detailed_result = detailed_result.replace('\n', '')
                      
                        detailed_result = detailed_result.replace('[', '')
                     
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Overpraising the West" in subcategory_result:
             
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Overpraising the West" The following are more detailed classification options: [NATO will destroy Russia][The West belongs in the right side of history][The West has the strongest international support].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                 
                        detailed_result = detailed_result.replace('\n', '')
                   
                        detailed_result = detailed_result.replace('[', '')
                 
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Speculating war outcomes" in subcategory_result:
                    
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Speculating war outcomes" The following are more detailed classification options: [Russian army is collapsing][Russian army will lose all the occupied territories][Ukrainian army is collapsing].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                   
                        detailed_result = detailed_result.replace('\n', '')
                 
                        detailed_result = detailed_result.replace('[', '')
                    
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Discrediting the West, Diplomacy" in subcategory_result:
                    
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Discrediting the West, Diplomacy." The following are more detailed classification options: [The EU is divided][The West is weak][The West is overreacting][The West does not care about Ukraine, only about its interests][Diplomacy does/will not work][West is tired of Ukraine].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
               
                        detailed_result = detailed_result.replace('\n', '')
                 
                        detailed_result = detailed_result.replace('[', '')
               
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Negative Consequences for the West" in subcategory_result:
                    
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Negative Consequences for the West" The following are more detailed classification options: [Sanctions imposed by Western countries will backfire][The conflict will increase the Ukrainian refugee flows to Europe].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                    
                        detailed_result = detailed_result.replace('\n', '')
                
                        detailed_result = detailed_result.replace('[', '')
             
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Distrust towards Media" in subcategory_result:
                  
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Distrust towards Media" The following are more detailed classification options: [Western media is an instrument of propaganda][Ukrainian media cannot be trusted].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                     
                        detailed_result = detailed_result.replace('\n', '')
                  
                        detailed_result = detailed_result.replace('[', '')
              
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Amplifying war-related fears" in subcategory_result:
                   
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Amplifying war-related fears" The following are more detailed classification options: [By continuing the war we risk WWIII][Russia will also attack other countries][There is a real possibility that nuclear weapons will be employed][NATO should/will directly intervene].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                   
                        detailed_result = detailed_result.replace('\n', '')
                 
                        detailed_result = detailed_result.replace('[', '')
           
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                elif "CC" in generated_text:
            
               
                    messages.append({"role": "user", "content": 'There are subcategories under "CC". Please select the appropriate subcategory that is relevant to the article. The subcategories are as follows: [Other][Criticism of climate policies][Criticism of institutions and authorities][Climate change is beneficial][Downplaying climate change][Questioning the measurements and science][Criticism of climate movement][Controversy about green technologies][Hidden plots by secret schemes of powerful groups][Amplifying Climate Fears][Green policies are geopolitical instruments].' + prompt})
            
                    completion = client.chat.completions.create(
                        model="gpt-4o",
                        messages=messages,
                        max_tokens=500,
                        temperature=0.0,
                    )
                    subcategory_result = completion.choices[0].message.content.strip()
          
                    subcategory_result = subcategory_result.replace('\n', '')
             
                    subcategory_result = subcategory_result.replace('[', '')
            
                    subcategory_result = subcategory_result.replace(']', ';')
                    f_out.write(f"{subcategory_result}\t")

             
                    if "Criticism of climate policies" in subcategory_result:
                   
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Criticism of climate policies" The following are more detailed classification options:[Climate policies are ineffective][Climate policies have negative impact on the economy][Climate policies are only for profit].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                 
                        detailed_result = detailed_result.replace('\n', '')
               
                        detailed_result = detailed_result.replace('[', '')
                  
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Green policies are geopolitical instruments" in subcategory_result:
                   
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Green policies are geopolitical instruments" The following are more detailed classification options:[Climate-related international relations are abusive/exploitative][Green activities are a form of neo-colonialism].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                       
                        detailed_result = detailed_result.replace('\n', '')
                  
                        detailed_result = detailed_result.replace('[', '')
                    
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Criticism of institutions and authorities" in subcategory_result:
                   
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Criticism of institutions and authorities" The following are more detailed classification options:[Criticism of the EU][Criticism of international entities][Criticism of national governments][Criticism of political organizations and figures].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                 
                        detailed_result = detailed_result.replace('\n', '')
            
                        detailed_result = detailed_result.replace('[', '')
             
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Climate change is beneficial" in subcategory_result:
                
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Climate change is beneficial" The following are more detailed classification options:[C02 is beneficial][Temperature increase is beneficial].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
               
                        detailed_result = detailed_result.replace('\n', '')
                
                        detailed_result = detailed_result.replace('[', '')
                
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Downplaying climate change" in subcategory_result:
                 
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Downplaying climate change" The following are more detailed classification options:[Climate cycles are natural][Weather suggests the trend is global cooling][Temperature increase does not have significant impact][C02 concentrations are too small to have an impact][Human activities do not impact climate change][Ice is not melting][Sea levels are not rising][Humans and nature will adapt to the changes].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
               
                        detailed_result = detailed_result.replace('\n', '')
                
                        detailed_result = detailed_result.replace('[', '')
                  
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Questioning the measurements and science" in subcategory_result:
                     
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Questioning the measurements and science" The following are more detailed classification options:[Methodologies/metrics used are unreliable/faulty][Data shows no temperature increase][Greenhouse effect/carbon dioxide do not drive climate change][Scientific community is unreliable].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                  
                        detailed_result = detailed_result.replace('\n', '')
                 
                        detailed_result = detailed_result.replace('[', '')
                
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Criticism of climate movement" in subcategory_result:
                    
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Criticism of climate movement" The following are more detailed classification options:[Climate movement is alarmist][Climate movement is corrupt][Ad hominem attacks on key activists].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                      
                        detailed_result = detailed_result.replace('\n', '')
                    
                        detailed_result = detailed_result.replace('[', '')
                     
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Controversy about green technologies" in subcategory_result:
                     
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Controversy about green technologies" The following are more detailed classification options:[Renewable energy is dangerous][Renewable energy is unreliable][Renewable energy is costly][Nuclear energy is not climate friendly].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                  
                        detailed_result = detailed_result.replace('\n', '')
                
                        detailed_result = detailed_result.replace('[', '')
                    
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Hidden plots by secret schemes of powerful groups" in subcategory_result:
             
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Hidden plots by secret schemes of powerful groups" The following are more detailed classification options:[Blaming global elites][Climate agenda has hidden motives].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
               
                        detailed_result = detailed_result.replace('\n', '')
                   
                        detailed_result = detailed_result.replace('[', '')
                   
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")

                    if "Amplifying Climate Fears" in subcategory_result:
                   
                        messages.append({"role": "user", "content": 'Please further categorize the specific content of "Amplifying Climate Fears" The following are more detailed classification options:[Earth will be uninhabitable soon][Amplifying existing fears of global warming][Doomsday scenarios for humans][Whatever we do it is already too late].' + prompt})
                        completion = client.chat.completions.create(
                            model="gpt-4o",
                            messages=messages,
                            max_tokens=500,
                            temperature=0.0,
                        )
                        detailed_result = completion.choices[0].message.content.strip()
                    
                        detailed_result = detailed_result.replace('\n', '')
                
                        detailed_result = detailed_result.replace('[', '')
                    
                        detailed_result = detailed_result.replace(']', '')
                        f_out.write(f"{detailed_result};")
