def decode_instruction(instruction: str) -> str:
    # Функция для декодирования сжатой инструкции

    stack: List[str] = []

    for char in instruction:
        if char == ']':
            decoded_str = ''
            while stack[-1] != '[':
                decoded_str = stack.pop() + decoded_str
            stack.pop()  # Удаляем '['

            num_str = ''
            while stack and stack[-1].isdigit():
                num_str = stack.pop() + num_str
            num = int(num_str)

            stack.append(decoded_str * num)
        else:
            stack.append(char)

    return ''.join(stack)


def main():
    compressed_instruction = input().strip()

    decoded_instruction = decode_instruction(compressed_instruction)
    print(decoded_instruction)


if __name__ == '__main__':
    main()
