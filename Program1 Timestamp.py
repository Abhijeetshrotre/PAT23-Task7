import datetime
def createfile_writefile():
    # Current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create file with current timestamp
    file_name = f"output_{current_timestamp}.txt"

    # Write the current timestamp to the file
    with open(file_name, 'w') as file:
        file.write(current_timestamp)

    print(f"File '{file_name}' created with content: {current_timestamp}")


#  create and write the file
createfile_writefile()