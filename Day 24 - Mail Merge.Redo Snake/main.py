
# # open a file, read and print contents.
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", mode="w") as file:  # mode "w" to rewrite the whole file. mode "a" for append!
    file.write("\nNew text.")