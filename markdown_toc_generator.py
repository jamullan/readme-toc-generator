# Readme Table of Contents Generator
# Copyright 2020 John Mullan
# The creator of this software, John Mullan, has made it available under the MIT license,
# as deliniated in the LICENSE file in the root directory of this repository
#
# Prints a hyperlinked table of contents for a supplied .md file to stdout

from sys import argv
import os

# generates headings from a supplied .md file
# file_name: the name of the README.md file to generate headings from
# detail_level: an integer between 1 and 6, inclusive, that determines
#       the most specific heading number to include
# returns: a 2D array of heading labels and levels of the type: [[<heading name>, <heading level>]]
def get_headings(file_name, detail_level):
    file = open(file_name, "r")
    headings = []
    
    heading_level = 0
    line_end = ""
    for line in file:
        try:
            split_line = str(line).split(" ", 1)
            line_begenning = split_line[0]
            line_end = split_line[1][:-1]
        except: #line can not be split, and is thus not a header
            continue

        heading_level = 0
        for char in line_begenning:
            if char != "#":
                break
            else:
                heading_level += 1

        if heading_level != len(line_begenning): #line is not a header
            continue

        elif heading_level <= detail_level:
            headings.append([line_end.rstrip(), heading_level])
    
    return headings

# verifies that the file exists and has the ".md" extension
# file_name: the name of the file to be verified
# returns: True if verified, False otherwise
def verify_file(file_name):
    try:
        assert ".md" in file_name, "The file must be a .md file"
    except AssertionError as error:
        os.system("clear")
        print(error)

        return False
    
    directory_path = os.path.dirname(os.path.abspath(__file__))
    try:
        if not os.path.exists(directory_path + "/" + file_name):
            raise FileNotFoundError("The supplied file \"{}\" does not exist in the directory of this program".format(file_name))

        return True

    except FileNotFoundError as error:
        os.system("clear")
        print(error)

        return False

# gets the filename of the README.md file (or similarily named file) to have a TOC generated for
# ignore_argv: a bool that if True will prompt the user for a filename
#       defaults to false, looking to argv[1] for the filename
# returns: the name of the file that the user would like to have a TOC generated for
def get_filename(ignore_argv = False):
    file_name = ""
    if not ignore_argv:
        try:
            file_name = argv[1]
            return file_name
        except IndexError:
            while True:
                file_name = input("Please supply a valid filename: ")
                if (file_name != ""):
                    break
            return file_name
    else:
        while True:
            file_name = input("Please supply a valid filename: ")
            if (file_name != ""):
                break

        return file_name

# provides a table of contents to std out
# headings: a 2D array of heading labels and levels of the type: [[<heading name>, <heading level>]]
# indent_factor: factor by which each element in the TOC will be indented by
def generate_toc(headings, indent_factor):
    toc_lines = []

    for heading in headings:
        indentation = ""
        for i in range((heading[1] - 1)*indent_factor):
            indentation += "&emsp;"
        title = "[" + heading[0] + "]"
        link = generate_link(heading[0])

        toc_line = indentation + title + link + "<br />"
        toc_lines.append(toc_line)

    os.system("clear")
    for toc_line in toc_lines:
        print(toc_line)

# generates a link for the supplied heading
# heading: the heading name to supply a link for
# returns: the heading's link
def generate_link(heading):
    link = ""
    for char in heading:
        if char == " ":
            link += "-"
        elif char == "&" or char == ":":
            link += ""
        else:
            link += char
    
    link = "(<#" + link + ">)"
        
    return link

# validates the DETAIL_LEVEL and INDENT_FACTOR, calls functions to obtain and verify a .md file
#       to generate a TOC for, and calls a function to generate the TOC
def main():
    '''
    the level 1 headers only (1) through all headings including level 6 (6)
    must be an integer value 1-6
    '''
    DETAIL_LEVEL = 6

    '''
    factor by which each level will be indented by
    must be an integer value 1-3
    '''
    INDENT_FACTOR = 1

    #validate the DETAIL_LEVEL
    try:
        assert type(DETAIL_LEVEL) == int
    except:
        raise ValueError("The set DETAIL_LEVEL of {} is invalid. It must be an integer".format(DETAIL_LEVEL))
    
    try:
        assert (DETAIL_LEVEL >= 1 and DETAIL_LEVEL <= 6)
    except:
        raise ValueError("The set DETAIL_LEVEL of {} is invalid. It must be between 1 and 6, inclusive".format(DETAIL_LEVEL))

    #validate the INDENT_FACTOR
    try:
        assert type(INDENT_FACTOR) == int
    except:
        raise ValueError("The set INDENT_FACTOR of {} is invalid. It must be an integer".format(DETAIL_LEVEL))
    try:
        assert (INDENT_FACTOR >= 1 and INDENT_FACTOR <= 3)
    except:
        raise ValueError("The set INDENT_FACTOR of {} is invalid. It must be between 1 and 3, inclusive".format(INDENT_FACTOR))

    #attempt to use argv[1] as the filename
    file_name = get_filename()
    file_verified = verify_file(file_name)

    #argv[1] in an invalid filename, and a valid .md filename has not been provided
    while not file_verified:
        file_name = get_filename(ignore_argv=True)
        file_verified = verify_file(file_name)
    
    headers = get_headings(file_name, DETAIL_LEVEL)
    generate_toc(headers, INDENT_FACTOR)

if __name__ == '__main__':
    main()