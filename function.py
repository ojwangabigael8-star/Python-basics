# functions methods
# print("Hello World") #built in
from custom_functions import greet

with open ("tempt.txt", "w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.34\n")

with open("tempt.txt", "r") as file:
    content = file.read()
    print(content)

# pip install yt-dlp
greet()