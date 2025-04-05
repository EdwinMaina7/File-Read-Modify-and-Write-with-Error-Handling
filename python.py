def read_and_modify_file():
    import os

    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the file for reading
        with open(filename, 'r') as file:
            contents = file.read()

        # Modify the content — example: convert to uppercase
        modified_contents = contents.upper()

        # Create new filename to write to
        new_filename = f"modified_{os.path.basename(filename)}"

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_contents)

        print(f"✅ File processed successfully! Modified content saved in '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
