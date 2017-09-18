import os

textpath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) \
    + "/../../../static/toltebot/text")

def get_file_list():
    file_list = []
    for dirpath, dirs, files in os.walk(textpath):
        for f in files:
            if '.html' in f:
                file_list.append(os.path.abspath(dirpath + "/" + f))
    return file_list

file_list = get_file_list()
