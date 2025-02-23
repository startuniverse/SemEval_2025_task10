def process_text_content():

    narritive_keywords = [
        "Other",
        "Blaming the war on others rather than the invader",
        "Discrediting Ukraine",
        "Russia is the Victim",
        "Praise of Russia",
        "Overpraising the West",
        "Speculating war outcomes",
        "Discrediting the West Diplomacy",
        "Negative Consequences for the West",
        "Distrust towards Media",
        "Amplifying war-related fears",
        "Hidden plots by secret schemes of powerful groups"
    ]
    narritive_keywordsCC = [
        "Other",
        "Criticism of climate policies",
        "Criticism of institutions and authorities",
        "Climate change is beneficial",
        "Downplaying climate change",
        "Questioning the measurements and science",
        "Criticism of climate movement",
        "Controversy about green technologies",
        "Hidden plots by secret schemes of powerful groups",
        "Amplifying Climate Fears",
        "Green policies are geopolitical instruments"
    ]

    subnarritive_keywords = [
        "Ukraine is the aggressor",
        "The West are the aggressors",
        "Rewriting Ukraine’s history",
        "Discrediting Ukrainian nation and society",
        "Discrediting Ukrainian military",
        "Discrediting Ukrainian government and officials and policies",
        "Ukraine is a puppet of the West",
        "Ukraine is a hub for criminal activities",
        "Ukraine is associated with nazism",
        "Situation in Ukraine is hopeless",
        "The West is russophobic",
        "Russia actions in Ukraine are only self-defence",
        "UA is anti-RU extremists",
        "Praise of Russian military might",
        "Praise of Russian President Vladimir Putin",
        "Russia is a guarantor of peace and prosperity",
        "Russia has international support from a number of countries and people",
        "Russian invasion has strong national support",
        "NATO will destroy Russia",
        "The West belongs in the right side of history",
        "The West has the strongest international support",
        "Russian army is collapsing",
        "Russian army will lose all the occupied territories",
        "Ukrainian army is collapsing",
        "The EU is divided",
        "The West is weak",
        "The West is overreacting",
        "The West does not care about Ukraine only about its interests",
        "Diplomacy does/will not work",
        "West is tired of Ukraine",
        "Sanctions imposed by Western countries will backfire",
        "The conflict will increase the Ukrainian refugee flows to Europe",
        "Western media is an instrument of propaganda",
        "Ukrainian media cannot be trusted",
        "By continuing the war we risk WWIII",
        "Russia will also attack other countries",
        "There is a real possibility that nuclear weapons will be employed",
        "NATO should/will directly intervene"
    ]
    subnarritive_keywordsCC = [
     "Climate policies are ineffective",
     "Climate policies have negative impact on the economy",
     "Climate policies are only for profit",
     "Climate-related international relations are abusive / exploitative",
     "Green activities are a form of neo-colonialism",
     "Criticism of the EU, Criticism of international entities",
     "Criticism of national governments",
     "Criticism of political organizations and figures",
     "C02 is beneficial",
     "Temperature increase is beneficial",
     "Climate cycles are natural",
     "Weather suggests the trend is global cooling",
     "Temperature increase does not have significant impact",
     "C02 concentrations are too small to have an impact",
     "Human activities do not impact climate change",
     "Ice is not melting, Sea levels are not rising",
     "Humans and nature will adapt to the changes",
     "Methodologies / metrics used are unreliable / faulty, Data shows no temperature increase",
     "Greenhouse effect / carbon dioxide do not drive climate change",
     "Scientific community is unreliable",
     "Climate movement is alarmist",
     "Climate movement is corrupt",
     "Ad hominem attacks on key activists",
     "Renewable energy is dangerous",
     "Renewable energy is unreliable",
     "Renewable energy is costly",
     "Nuclear energy is not climate friendly",
     "Blaming global elites",
     "Climate agenda has hidden motives",
     "Earth will be uninhabitable soon",
     "Amplifying existing fears of global warming",
     "Doomsday scenarios for humans",
     "Whatever we do it is already too late"

    ]


    input_file = "/root/autodl-tmp/ai/test/output/S2PT4o.txt"
    output_file = "/root/autodl-tmp/ai/test/output/S2PT4oF1.txt"

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
     
            parts = line.strip().split('\t')
            if len(parts) != 3:
                print(f"error: {line.strip()}")
                continue

            filename, narritive, subnarritive = parts
            if narritive.startswith("URW"):
   
                matched_narritive = []
                for keyword in narritive_keywords:
                    if keyword in narritive:
                        matched_narritive.append("URW: "+keyword+";")
                new_narritive ="".join(matched_narritive) if matched_narritive else narritive
                if new_narritive.endswith(";"):
                    new_narritive = new_narritive[:-1]
                else:
                    new_narritive = new_narritive

          
                matched_subnarritive = []
                for keyword in subnarritive_keywords:
                    if keyword in subnarritive:
                        matched_subnarritive.append("URW: "+keyword+";")
                new_subnarritive = "".join(matched_subnarritive) if matched_subnarritive else subnarritive
                if new_subnarritive.endswith(";"):
                    new_subnarritive = new_subnarritive[:-1]
                else:
                    new_subnarritive = new_subnarritive
                outfile.write(f"{filename}\t{new_narritive}\t{new_subnarritive}\n")

 

            elif narritive.startswith("CC"):

                matched_narritiveCC = []
                for keyword in narritive_keywordsCC:
                    if keyword in narritive:
                        matched_narritiveCC.append("CC: "+keyword+";")
                new_narritiveCC ="".join(matched_narritiveCC) if matched_narritiveCC else narritive
                if new_narritiveCC.endswith(";"):
                    new_narritiveCC = new_narritiveCC[:-1]
                else:
                    new_narritiveCC = new_narritiveCC



                matched_subnarritiveCC = []
                for keyword in subnarritive_keywordsCC:
                    if keyword in subnarritive:
                        matched_subnarritiveCC.append("CC: "+keyword+";")
                new_subnarritiveCC ="".join(matched_subnarritiveCC) if matched_subnarritiveCC else subnarritive
                if new_subnarritiveCC.endswith(";"):
                    new_subnarritiveCC = new_subnarritiveCC[:-1]
                else:
                    new_subnarritiveCC = new_subnarritiveCC
                outfile.write(f"{filename}\t{new_narritiveCC}\t{new_subnarritiveCC}\n")


if __name__ == "__main__":
    process_text_content()
