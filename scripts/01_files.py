# open a text file
input_file = open("files/random.txt")

# read lines and print
for word in input_file.readlines():
    print(word)

# reset read pointer
input_file.seek(0)

# open a file in write mode
output_file = open("files/output.txt", "w")

txt = input_file.read()

words = set(map(lambda x: x.strip(' ,.').lower(), txt.split()))

for word in words:
    output_file.write(word + "\n")
