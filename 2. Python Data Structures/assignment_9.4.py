"""
9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those
lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"

emails_count = dict()

with open(name) as fh:
    for line in fh:
        if line.startswith('From '):
            key = line.split()[1]

            if key not in emails_count:
                emails_count[key] = 0
            emails_count[key] += 1

max_value = max(emails_count.values())
max_key = [k for k, v in emails_count.items() if v == max_value]

print(max_key[0], max_value)