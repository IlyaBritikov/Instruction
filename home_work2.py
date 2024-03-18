def decode_instruction(instruction: str) -> str:
    # Функция для декодирования сжатой инструкции

    stack: List[str] = []

    for char in instruction:
        if char == ']':
            decoded_str = ''
            for sign in stack[::-1]:
                if sign == '[':
                    stack.pop()  # Удаляем '['
                    break
                else:
                    decoded_str = stack.pop() + decoded_str

            num_str = ''
            for sign in stack[::-1]:
                if sign.isdigit():
                    num_str = stack.pop() + num_str
                else:
                    break
            num = int(num_str)

            stack.append(decoded_str * num)
        else:
            stack.append(char)

    decode_instruction = ''
    for item in stack:
        if isinstance(item, tuple):
            decode_instruction += item[0] * item[1]
        else:
            decode_instruction += item
    return decode_instruction            

def main():
    compressed_instruction = input().strip()

    decoded_instruction = decode_instruction(compressed_instruction)
    print(decoded_instruction)


if __name__ == '__main__':
    main()
