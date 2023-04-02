import os


class FileIO:
    def __init__(self, filename):
        self.filename = filename

        print(self.filename)
        # Check if the file exists
        if os.path.exists(self.filename):
            # Delete the file if it exists
            os.remove(self.filename)
        #print("File I/O initialized.")

    def write_formatted_message(self, message):
        try:
            with open(self.filename, "a") as file:
                file.write(message + "\n")
            # print("Formatted message written successfully.")
        except IOError:
            print("An error occurred while writing the file.")
