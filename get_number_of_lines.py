def get_number_of_lines(file_path) -> int:
    with open(file_path, 'r', encoding='utf8') as file:
        line_count = 0
        for _ in file:
            line_count += 1
    return line_count