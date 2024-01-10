#!/usr/bin/python3

"""script that adds all arguments to a list,and then save them to a file"""

import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

for i in range(1, len(sys.argv)):
    if os.path.isfile("add_item.json"):
        my_list = load_from_json_file("add_item.json")
        my_list.append(sys.argv[i])
        save_to_json_file(my_list, "add_item.json")
    else:
        my_list = []
        my_list.append(sys.argv[i])
        save_to_json_file(my_list, "add_item.json")
