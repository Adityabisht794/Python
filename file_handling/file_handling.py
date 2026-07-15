file_name=input("Enter the file name: ")
try:
    f_handle=open(file_name,"r+")
except Exception as e:
    print("File cannot be opened:", e)
    quit()

count=0

for line in f_handle:
    count=count+1
    print(line)

print("\nThere were", count, "lines in", file_name)

print("\n")
f_handle.seek(0)  # Reset file pointer to the beginning of the file
count=0

for line in f_handle:
    if line.startswith("-"):
        count=count+1

print("There were", count, "- lines in", file_name)

f_handle.seek(0)  
for line in f_handle:
    if line.startswith("-"):
        line="*" + line[1:] 
        print(line) 
    

lines=["\nThis is a new line 1\n", "This is a new line 2\n", "This is a new line 3\n"]
f_handle.writelines(lines)

f_handle.seek(0)  # Reset file pointer to the beginning of the file
print("\nUpdated file content:")
for line in f_handle:
    print(line)

f_handle.close()