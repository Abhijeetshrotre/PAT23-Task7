def read_filepath():
    # Provide the absolute path to the file
    file_path = "d:\\test.txt"

    # Open the file in read only mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Display the content
        print("File Content:")
        print(file_content)

# Call the function
read_filepath()