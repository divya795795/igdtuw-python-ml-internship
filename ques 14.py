lines = []

print("Enter lines of text (press Enter on an empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)
