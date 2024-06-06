import sys
import converter

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith('.json'):
        data = converter.load_json(input_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        data = converter.load_yaml(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)

    converter.save_json(data, output_file)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
