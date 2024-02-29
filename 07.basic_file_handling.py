# Basic File Handling
def file_handling():
    # Specify the file path
    file_path = 'example.txt'

    # Writing to a file
    with open(file_path, 'a') as file:    # 'a" is used means it writes file and append without deleting the old data.
        file.write('Hello, the text was written.\n')

    # Reading from a file
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        print(content)

# Run the File Handling
file_handling()
