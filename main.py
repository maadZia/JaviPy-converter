from converter import convert
def main(input_file, output_file):
    with open(input_file, 'r') as file:
        input_text = file.read()

    converted_code = convert(input_text)

    with open(output_file, 'w') as file:
        file.write(converted_code)

if __name__ == "__main__":
    input_file = "example/test.txt"
    output_file = "output.py"
    main(input_file, output_file)


