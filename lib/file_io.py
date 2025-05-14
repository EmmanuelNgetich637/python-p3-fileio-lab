def write_file(file_name, file_content):
    with open(f"{file_name}.txt","w") as file:
        #Write the content provided in the file_content argument tothe file.
        file.write(file_content)

def append_file(file_name, append_content):
    #Open the file in append mode ("a") to add content without overwriting.
    #Adding ".txt ensures we're working with the correct file extension"
    with open(f"{file_name}.txt", "a") as file:
              file.write(append_content)

def read_file(file_name):
    #Open the file in read mode ("r") to fetch its own contents.
    with open(f"{file_name}.txt", "r") as file:
         #Read the entire content of the file and return it.
         return file.read() 
