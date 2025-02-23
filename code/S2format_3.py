def process_line(line):
    try:
        filename, coarse, fine = line.strip().split('\t')
    except ValueError:
        print(f"Skipping invalid line: {line.strip()}")
        return line 
        

    coarse_entries = coarse.split(';')
    content_to_prefix = {}
    for entry in coarse_entries:
        if ':' in entry:
            prefix, content = entry.split(':', 1)
            content_to_prefix[content.strip()] = prefix.strip()
        else:
            print(f"Invalid coarse entry format: {entry}")
    

    fine_entries = fine.split(';')
    new_fine_entries = []
    
    for f_entry in fine_entries:
        if ':' not in f_entry:
            print(f"Invalid fine entry format: {f_entry}")
            new_fine_entries.append(f_entry)
            continue
            
        category, description = f_entry.split(':', 1)
        prefix = content_to_prefix.get(category.strip())
        
        if prefix:
            new_entry = f"{prefix}: {category.strip()}: {description.strip()}"
            new_fine_entries.append(new_entry)
        else:
            print(f"No matching coarse category found for: {category}")
            new_fine_entries.append(f_entry)
    
    return f"{filename}\t{coarse}\t{';'.join(new_fine_entries)}\n"

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            processed_line = process_line(line)
            f_out.write(processed_line)

if __name__ == "__main__":
    input_filename = "/root/autodl-tmp/ai/test/output/S2PT4oF2.txt"  
    output_filename = "/root/autodl-tmp/ai/test/output/S2PT4oF3.txt"  
    main(input_filename, output_filename)
