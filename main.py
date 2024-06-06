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
    elif input_file.endswith('.xml'):
        data = converter.load_xml(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)

    if output_file.endswith('.json'):
        converter.save_json(data, output_file)
    elif output_file.endswith('.yaml') or output_file.endswith('.yml'):
        converter.save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        converter.save_xml(data, output_file)
    else:
        print("Unsupported output file format")
        sys.exit(1)

    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
