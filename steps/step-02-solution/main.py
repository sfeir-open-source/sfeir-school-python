import sys

def main():
    input_file_path = "folder/input.txt"
    output_file_path = "folder/output.txt"
    if len(sys.argv) > 1:
        # Open files
        input_file = open(input_file_path, mode='r')
        output_file = open(output_file_path, mode='a')
        txt_found_in_file = False
        # Input Args
        input_txt = sys.argv[1]
        # Read lines
        for line in input_file:
            if input_txt in line:
                txt_found_in_file = True
        # If input is not in input file
        if not txt_found_in_file:
            # Write line
            output_file.writelines(f"{input_txt}\n")

        # Close files
        input_file.close() 
        output_file.close()


if __name__ == "__main__":
    main()