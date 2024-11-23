import sys

def display_help():
    print('Please enter the following commands to manipulate files: reverse, copy, duplicate-contents, or replace-string.')
    print('If you enter "python3 file_manipulator.py reverse <input file path> <output file path>", the command reverses the contents of the input file.')
    print('If you enter "python3 file_manipulator.py copy <input file path> <output file path>", the command copies the input file as the output file.')
    print('If you enter "python3 file_manipulator.py duplicate-contents <input file path> n", the command leads the contents of the input file to duplicate it and write it n times to the input file.')
    print('If you enter "python3 file_manipulator.py replace-string <input file path> <needle> <new_string>", the command searches the string you specified with <needle> from the input file to replace all of <needle> into <new_string>.')

if len(sys.argv) < 4:
    display_help()
    sys.exit(1)

else:
    command = sys.argv[1]
    input_pathname = sys.argv[2]
    contents = ''

    if command == 'reverse':
        output_pathname = sys.argv[3]

        with open(input_pathname, 'r') as input_file:
            contents = input_file.read()

        with open(output_pathname, 'w') as output_file:
            output_file.write(contents[::-1])

    elif command == 'copy':
        output_pathname = sys.argv[3]

        with open(input_pathname, 'r') as input_file:
            contents = input_file.read()

        with open(output_pathname, 'w') as output_file:
            output_file.write(contents)

    elif command == 'duplicate-contents':
        number_of_copies = sys.argv[3]

        if not number_of_copies.isdecimal():
            print('Please enter a number after the input file path.')
            sys.exit(1)

        else:
            number_of_copies = int(number_of_copies)

        with open(input_pathname, 'r') as file:
            contents = file.read()

        with open(input_pathname, 'a') as file:
            for i in range(number_of_copies):
                file.write(contents)

    elif command == 'replace-string':
        if len(sys.argv) < 5:
            print('Please enter the string you want to replace and the new string you want to replace with.')
            sys.exit(1)

        with open(input_pathname, 'r') as file:
            contents = file.read()

        with open(input_pathname, 'w') as file:
            file.write(contents.replace(sys.argv[3], sys.argv[4]))

    else:
        display_help()
        sys.exit(1)

    print('The file has been manipulated successfully.')
    sys.exit(0)
