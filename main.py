# main.py
import sys
import converter

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = converter.load_json(input_file)
    print(f"Data: {data}")

if __name__ == "__main__":
    main()