import os
import csv
import random
import re

# Read and print: The full content, First 20 characters, First line, All lines as a list.
def reading():
    # opened them separately because it was being already read before

    # full content
    with open('data/sample.txt', 'r') as f1:
        f1content = f1.read()
        print("Printing the full content of sample.txt:")
        print(f1content)

    # first 20 chars
    with open('data/sample.txt', 'r') as f1:
        f1_20 =  f1.read(20)
        print("\nPrinting the first 20 characters of sample.txt: ")
        print(f1_20)

    # first line
    with open('data/sample.txt', 'r') as f1:
        f1_line = f1.readline()
        print("\nPrinting the first line of sample.txt: ")
        print(f1_line)

    # all lines as a list
    with open('data/sample.txt', 'r') as f1:
        f1contentlist = f1.readlines()
        print("\nPrinting the content of sample.txt: ")
        print(f1contentlist)


# Copy the contents of sample.txt to copy_target.txt.txt using read/write in a context manager.
def copy():
    with open('data/sample.txt', 'r') as f1_read:
        with open('data/copy_target.txt', 'w') as f1_write:
            for line in f1_read:
                f1_write.write(line)

    print("\nCopied sample.txt")


# Rename files: Inside reports, Rename them to report-1.txt, report-2.txt, etc.
def rename_files():
    os.chdir('data/reports')

    try:
        for f in os.listdir():
            file_name, file_ext = os.path.splitext(f)

            file_name = file_name.title()
            name, no = file_name.split('-')
            no = no.zfill(2)
            new_name = f'{name}_{no}' + file_ext

            os.rename(f, new_name)

        print("\nRenamed reports")
    except:
        print("\nReport names have already been renamed.")


# Parse CSV file: Read people.csv using csv.DictReader.
# Randomly assign each person in people.csv a greeting (Hi, Hello, Hey). Save this to a new CSV file greetings.csv.
def greet():
    os.chdir('..')
    print("Creating 3 files to show randomness.")
    for i in range(3):
        with open('people.csv', 'r') as f2_read:
            csv_reader = csv.DictReader(f2_read)
            rows = list(csv_reader)

            greetings = ['Hi', 'Hello', 'Hey', 'Hola']

            with open(f'greetings{i+1}.csv', 'w', newline='') as f2_write:
                csv_writer = csv.writer(f2_write)

                for row in rows:
                    greeting = random.choice(greetings)
                    name = row['name']
                    csv_writer.writerow([greeting, name])

            print(f"\nGreetings {i+1} done. ")


# Regex (Bonus): Use regex to extract all email usernames (before the '@') from people.csv.
def getUsernames():
    with open('people.csv', 'r') as f2_read:
        csv_reader = csv.DictReader(f2_read)
        rows = list(csv_reader)
        usernames = []

        for row in rows:
            email = str(row['email'])

            pattern = re.compile(r'(.+)@')
            matches = pattern.findall(email)
            for match in matches:
                usernames.append(match)

        print(usernames)



def main():
    print("-" * 40)
    print("Reading sample.txt: ")
    reading()

    print("-" * 40)
    print("Copying sample.txt: ")
    copy()

    print("-" * 40)
    print("Renaming reports: ")
    rename_files()

    print("-" * 40)
    print("Greetings: ")
    greet()

    print("-" * 40)
    print("Getting usernames: ")
    getUsernames()

main()



