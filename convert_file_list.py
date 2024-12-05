import os

def modify_file_list(input_file, output_file, text_to_add):
    """
    Reads a file containing a list of file paths, appends the file name and additional text
    to each path, and writes the modified list to a new file.

    Parameters:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
        text_to_add (str): Text to append to each path, combined with the file name.
    """
    try:
        # Read the list of file paths from the input file
        with open(input_file, 'r') as infile:
            file_paths = infile.readlines()

        # Process each file path
        modified_file_paths = []
        for path in file_paths:
            path = path.strip()  # Remove leading/trailing whitespace
            file_name = os.path.basename(path)  # Extract the file name
            # Append the file name to the text_to_add variable
            modified_entry = f"{path} {text_to_add}{file_name}\n"
            modified_file_paths.append(modified_entry)

        # Write the modified list to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_file_paths)

        print(f"Modified file list has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "list252068.txt"  # Input file containing the list of file names
    output_file = "plist_252068.txt"  # Output file for the modified list
    text_to_add = "/global/cfs/cdirs/m1657/enochjo/goamazon/arm/maovisstpx2dg13minnisX1.c1/"  # Text to append to each file name

    modify_file_list(input_file, output_file, text_to_add)
