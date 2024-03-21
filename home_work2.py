def decode_instruction(instruction: str) -> str:
    stack = []
    current_str = ''
    current_num = 0

    for char in instruction:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, prev_num = stack.pop()
            current_str = prev_str + current_str * prev_num
        else:
            current_str += char

    return current_str

# Считываем сжатую команду из ввода
compressed_instruction = input().strip()

# Расшифровываем команду и выводим результат
decoded_instruction = decode_instruction(compressed_instruction)
print(decoded_instruction)
