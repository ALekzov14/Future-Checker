def remove_matching_lines(file1, file2, output_file):
    with open(file2, 'r', encoding='utf-8') as f:
        lines_to_remove = set(f.read().splitlines())

    unique_lines = set()

    with open(file1, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line not in lines_to_remove:
                unique_lines.add(stripped_line)

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in unique_lines:
            f.write(line + '\n')


file1 = '../txt/output_for_bad_romover_nursultan.txt'
file2 = '../txt/badaccs_nursultan.txt'
output_file = '../txt/output_nursultan.txt'

remove_matching_lines(file1, file2, output_file)
