# Basic File Handling
def file_handling():
    # Specify the file path
    file_path = 'example.txt'

    # Writing to a file using 'w+' (Write and Read) mode (creating or truncating the file)
    with open(file_path, 'w+') as file:
        file.write('Hello, this is written using w+ mode.\n')
        file.seek(0)  # Move the file pointer to the beginning

        # Reading from a file using 'r+'(Read and Write) mode
        content = file.read()
        print(f'Content using w+ mode: {content}')

    # Appending to a file using 'a' mode
    with open(file_path, 'a') as file:
        file.write('This is appended using a mode.\n')

    # Reading from a file using 'r' mode
    with open(file_path, 'r') as file:
        content = file.read()
        print(f'Final content: {content}')

# Run the File Handling
file_handling()
