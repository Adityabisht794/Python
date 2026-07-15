print("Enter the file name:")
file_name = input()

try:
    f_handle = open(file_name, "r+")
except Exception as e:
    print("Error:", e)
    quit()

temp = f_handle.read()

print("File content:\n")
print(repr(temp))

count = 0
demo = ""

for ch in temp:
    demo += ch

    if ch == "\n":
        count += 1

        if count == 4:
            print(demo, end="")
            print("-" * 40)
            demo = ""
            count = 0

# Print any remaining content after the loop
if demo:
    print(demo, end="")

f_handle.close()
