print("Enter file name:")
file_name = input()

try:
    f_handle = open(file_name, "r")
except Exception as e:
    print("Error:", e)
    quit()

count = {}

# Count frequencies
for line in f_handle:
    if line.startswith("From:"):
        temp = line.split()[1]
        count[temp] = count.get(temp, 0) + 1

print(count)

f_handle.seek(0)

emails = {}

current_sender = None
current_email = ""

for line in f_handle:

    if line.startswith("From:"):

        if current_sender is not None:
            emails.setdefault(current_sender, []).append(current_email)

        current_sender = line.split()[1]
        current_email = line

    else:
        current_email += line

# Save the last email
if current_sender is not None:
    emails.setdefault(current_sender, []).append(current_email)

f_handle.close()

import os

folder = "Sorted_Emails"

if not os.path.exists(folder):
    os.mkdir(folder)

for sender, email_list in emails.items():

    filename = sender.replace("@", "_") + ".txt"

    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as out:
        for email in email_list:
            out.write(email)
            out.write("\n")

f_handle.close()
