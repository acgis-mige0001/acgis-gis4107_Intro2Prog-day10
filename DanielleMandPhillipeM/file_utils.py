#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      elle.migeon
#
# Created:     12-11-2019
# Copyright:   (c) elle.migeon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
def main():
    pass

def get_file_content(file_name):
    script_folder = ""
    """Read content from an existing file"""
    """Try to read content from a non-existant file. Trap the IOError."""
    try:
        with open(file_name) as in_file:
            content = in_file.read()
        return content
    except IOError:
        return '{} does not exist'.format (file_name)


def write_to_file (file_name, content):
    """Write content to an existing file"""
    with open (file_name, "w") as out_file:
        out_file.write("Thank you")
    return file_name, content

if __name__ == '__main__':
    main()