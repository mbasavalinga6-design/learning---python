# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is my first file handling program.\n")
    file.write("Learning Python step by step.\n")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
