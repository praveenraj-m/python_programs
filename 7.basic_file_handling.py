# Basic File Handling
def file_handling():
    file_path = 'example.txt'

    # Writing to a file
    with open(file_path, 'w') as file:
        file.write('Hello, this is a sample file.\n')

    # Reading from a file
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

# Run the File Handling
file_handling()
