from converter import convert, ConversionError

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        input_text = file.read()

    try:
        converted_code = convert(input_text)
    except SyntaxError as e:
        raise ConversionError(str(e))
    except Exception as e:
        raise ConversionError(f"Unexpected error during conversion: {str(e)}")

    with open(output_file, 'w') as file:
        file.write(converted_code)

if __name__ == "__main__":
    input_file = "example/test.java"
    output_file = "output.py"
    main(input_file, output_file)
