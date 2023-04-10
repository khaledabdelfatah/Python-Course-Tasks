def count_uppercase_chars(input_file, output_file):
    with open(input_file, 'r') as f1, open(output_file, 'w') as f2:
        content = f1.read()
        uppercase_count = sum(1 for c in content if c.isupper())
        f2.write(f"The number of uppercase characters in {input_file} is {uppercase_count}")

count_uppercase_chars("file2.txt", "filewithccounts.txt")
