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
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    with open (file_name) as in_file:
            content = in_file.read()
    return content

def get_missing_file_content(file_name):
    try:
        with open(file_name) as in_file:
            content = in_file.read()
        return content
    except IOError:
        return '{} does not exist'.format (file_name)

if __name__ == '__main__':
    main()