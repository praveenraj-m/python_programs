# Basic File Handling with Different Modes
def file_handling_with_modes():
    # Specify the file path
    file_path = 'example.txt'

    # 'r' mode (Read): Opens the file for reading
    with open(file_path, 'r') as file:
        content_read = file.read()
        print(f"Content using 'r' mode: {content_read}")

    # 'w' mode (Write): Opens the file for writing (creates a new file or truncates the existing file)
    with open(file_path, 'w') as file:
        file.write('This is written using \'w\' mode.\n')

    # 'r+' mode (Read and Write): Opens the file for both reading and writing
    with open(file_path, 'r+') as file:
        content_read_write = file.read()
        print(f"Content using 'r+' mode before write: {content_read_write}")

        # Write additional content
        file.write('This is written using \'r+\' mode.\n')
        file.seek(0)  # Move the file pointer to the beginning

        # Read the updated content
        content_after_write = file.read()
        print(f"Content using 'r+' mode after write: {content_after_write}")

    # 'w+' mode (Write and Read): Opens the file for both writing and reading (creates a new file or truncates the existing file)
    with open(file_path, 'w+') as file:
        file.write('This is written using \'w+\' mode.\n')
        file.seek(0)  # Move the file pointer to the beginning

        # Read the content
        content_write_read = file.read()
        print(f"Content using 'w+' mode: {content_write_read}")

    # 'a' mode (Append): Opens the file for appending (creates a new file if it doesn't exist)
    with open(file_path, 'a') as file:
        file.write('This is appended using \'a\' mode.\n')

    # Reading from a file using 'r' mode
    with open(file_path, 'r') as file:
        final_content = file.read()
        print(f'Final content: {final_content}')

# Run the File Handling with Different Modes
file_handling_with_modes()
