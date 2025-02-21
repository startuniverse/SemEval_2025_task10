def process_text_content():
    # 完整分类映射关系（根据参考代码所有分支构建）
    category_mapping = {
        "URW": {
            # URW分类体系
            "Blaming the war on others rather than the invader": [
                "Ukraine is the aggressor",
                "The West are the aggressors"
            ],
            "Discrediting Ukraine": [
                "Rewriting Ukraine’s history",
                "Discrediting Ukrainian nation and society",
                "Discrediting Ukrainian military",
                "Discrediting Ukrainian government and officials and policies",
                "Ukraine is a puppet of the West",
                "Ukraine is a hub for criminal activities",
                "Ukraine is associated with nazism",
                "Situation in Ukraine is hopeless"
            ],
            "Russia is the Victim": [
                "The West is russophobic",
                "Russia actions in Ukraine are only self-defence",
                "UA is anti-RU extremists"
            ],
            "Praise of Russia": [
                "Praise of Russian military might",
                "Praise of Russian President Vladimir Putin",
                "Russia is a guarantor of peace and prosperity",
                "Russia has international support from a number of countries and people",
                "Russian invasion has strong national support"
            ],
            "Overpraising the West": [
                "NATO will destroy Russia",
                "The West belongs in the right side of history",
                "The West has the strongest international support"
            ],
            "Speculating war outcomes": [
                "Russian army is collapsing",
                "Russian army will lose all the occupied territories",
                "Ukrainian army is collapsing"
            ],
            "Discrediting the West Diplomacy": [
                "The EU is divided",
                "The West is weak",
                "The West is overreacting",
                "The West does not care about Ukraine only about its interests",
                "Diplomacy does/will not work",
                "West is tired of Ukraine"
            ],
            "Negative Consequences for the West": [
                "Sanctions imposed by Western countries will backfire",
                "The conflict will increase the Ukrainian refugee flows to Europe"
            ],
            "Distrust towards Media": [
                "Western media is an instrument of propaganda",
                "Ukrainian media cannot be trusted"
            ],
            "Amplifying war-related fears": [
                "By continuing the war we risk WWIII",
                "Russia will also attack other countries",
                "There is a real possibility that nuclear weapons will be employed",
                "NATO should/will directly intervene"
            ]
        },
        "CC": {
            # CC分类体系
            "Hidden plots by secret schemes of powerful groups": [
                "Blaming global elites",
                "Climate agenda has hidden motives"
            ],
            "Criticism of climate policies": [
                "Climate policies are ineffective",
                "Climate policies have negative impact on the economy",
                "Climate policies are only for profit"
            ],
            "Green policies are geopolitical instruments": [
                "Climate-related international relations are abusive / exploitative",
                "Green activities are a form of neo-colonialism"
            ],
            "Criticism of institutions and authorities": [
                "Criticism of the EU",
                "Criticism of international entities",
                "Criticism of national governments",
                "Criticism of political organizations and figures"
            ],
            "Climate change is beneficial": [
                "C02 is beneficial",
                "Temperature increase is beneficial"
            ],
            "Downplaying climate change": [
                "Climate cycles are natural",
                "Weather suggests the trend is global cooling",
                "Temperature increase does not have significant impact",
                "C02 concentrations are too small to have an impact",
                "Human activities do not impact climate change",
                "Ice is not melting, Sea levels are not rising",
                "Humans and nature will adapt to the changes"
            ],
            "Questioning the measurements and science": [
                "Methodologies / metrics used are unreliable / faulty",
                "Data shows no temperature increase",
                "Greenhouse effect / carbon dioxide do not drive climate change",
                "Scientific community is unreliable"
            ],
            "Criticism of climate movement": [
                "Climate movement is alarmist",
                "Climate movement is corrupt",
                "Ad hominem attacks on key activists"
            ],
            "Controversy about green technologies": [
                "Renewable energy is dangerous",
                "Renewable energy is unreliable",
                "Renewable energy is costly",
                "Nuclear energy is not climate friendly"
            ],
            "Amplifying Climate Fears": [
                "Earth will be uninhabitable soon",
                "Amplifying existing fears of global warming",
                "Doomsday scenarios for humans",
                "Whatever we do it is already too late"
            ]
        }
    }

    # 文件处理
    # 定义文件路径（请确认路径正确性）
    input_file = "/root/autodl-tmp/ai新/test/output/S2PT4oF1.txt"
    output_file = "/root/autodl-tmp/ai新/test/output/S2PT4oF2.txt"

    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
            line = line.strip()
            if not line:
                continue

            try:
                # 解析字段
                filename, narritives_str, subnarritives_str = line.split('\t')

                # 处理主分类（支持多个）
                coarse_categories = []
                for narritive in narritives_str.split(';'):
                    if ':' in narritive:
                        _, coarse_value = narritive.split(':', 1)
                        coarse_categories.append(coarse_value.strip())

                # 处理子分类
                processed_subs = []
                for sub in subnarritives_str.split(';'):
                    # 清洗子分类值
                    sub_clean = sub.split(':', 1)[-1].strip() if ':' in sub else sub.strip()
                    matched = False

                    # 遍历所有主分类寻找匹配
                    for coarse_value in coarse_categories:
                        # 获取分类类型（CC/URW）
                        narritive_type = "CC" if "CC:" in sub else "URW"  # 根据实际情况调整

                        if (coarse_value in category_mapping[narritive_type] and
                                sub_clean in category_mapping[narritive_type][coarse_value]):
                            processed_subs.append(f"{coarse_value}: {sub_clean}")
                            matched = True
                            break

                    if not matched:
                        processed_subs.append(sub)  # 保留原始格式

                # 构建新行
                new_line = f"{filename}\t{narritives_str}\t{';'.join(processed_subs)}"
                outfile.write(new_line + '\n')

            except Exception as e:
                print(f"处理行出错: {line} | 错误: {str(e)}")
                outfile.write(line + '\n')  # 保留原始行


if __name__ == "__main__":
    process_text_content()