import json

# Replace 'your_file.json' with the path to your actual JSON file
input_file_path = 'finetune.json'
# Specify the output JSONL file name
output_file_path = 'output_file.jsonl'

# Open the input JSON file and load it into a Python object
with open(input_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Open the output file in write mode
with open(output_file_path, 'w', encoding='utf-8') as jsonl_file:
    # Iterate over each item in the list (assuming your JSON is a list of objects)
    for item in data:
        # Convert each item to a JSON string and write it to the file with a newline
        jsonl_file.write(json.dumps(item) + '\n')
