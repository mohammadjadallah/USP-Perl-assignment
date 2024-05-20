import sys
import os
from os import access, R_OK
from os.path import isfile

def unix_Systems_Programming(opt, argument_file, lang=None):
    if opt == '-v':
        print("Name: Mohammad Adnan")
        print("Surname: Salameh")
        print("Student ID: 32007454062")
        print("Date of Completion: 2024-05-17")
        return

    file_path = fr"{argument_file}"

    assert isfile(file_path) and access(file_path, R_OK), \
        f"File {file_path} doesn't exist or isn't readable"

    with open(argument_file, "r") as f:
        lines = f.readlines()

    locale_exist = any('locale' in line for line in lines)
    charmaps_exist = any('charmap' in line for line in lines)

    if opt == '-a':
        if not locale_exist:
            print("No locales available")
        else:
            print("Available locales:")
            for line in lines:
                values = line.split(",")
                if values[0] == "locale":
                    print(values[2], end="")

    elif opt == '-m':
        if not charmaps_exist:
            print("No charmaps available")
        else:
            print("Available charmaps:")
            for line in lines:
                values = line.split(",")
                if values[0] == "charmap":
                    print(values[2], end="")

    elif opt == '-l' and lang:
        count_locales = 0
        count_charmaps = 0

        for line in lines:
            values = line.split(",")
            if values[1] == lang:
                if values[0] == "locale":
                    count_locales += 1
                if values[0] == "charmap":
                    count_charmaps += 1

        if count_locales == 0 and count_charmaps == 0:
            print("No locales or charmaps in this language")
        else:
            print(f"Language {lang}:")
            print(f"Total number of locales: {count_locales}")
            print(f"Total number of charmaps: {count_charmaps}")

    else:
        print("Invalid syntax or missing arguments.")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python locale.py <option> <argument_file> [language]")
        sys.exit(1)

    option = sys.argv[1]
    if option not in ['-a', '-m', '-l', '-v']:
        print("Invalid option.")
        sys.exit(1)

    if option == '-l' and len(sys.argv) == 4:
        language = sys.argv[2]
        argument_file = sys.argv[3]
    elif option in ['-a', '-m', '-v'] and len(sys.argv) == 3:
        language = None
        argument_file = sys.argv[2]
    else:
        print("Usage: python locale.py <option> <argument_file> [language]")
        sys.exit(1)

    print(f"[INFO]: Option Used By User: {option}")
    print(f"[INFO]: argument_file Used By User: {argument_file}")
    if language:
        print(f"[INFO]: Language Used By User: {language}")

    unix_Systems_Programming(option, argument_file, language)
