#!/usr/bin/python3

""" write file module"""


def write_file(filename="", text=""):
    """ write file function"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
