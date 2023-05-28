#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     28/05/2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def get_file_types(extension_types, filenames):
    extension_type_dict = {}
    result_dict = {}

    # Create a dictionary mapping extensions to types
    for item in extension_types.split(';'):
        extension, file_type = item.split(',')
        extension_type_dict[extension] = file_type

    # Determine the type of each filename
    for filename in filenames:
        extension = filename.split('.')[-1]
        if extension in extension_type_dict:
            result_dict[filename] = extension_type_dict[extension]
        else:
            result_dict[filename] = 'unknown'

    return result_dict
extension_types = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_types(extension_types, filenames)
print(result)