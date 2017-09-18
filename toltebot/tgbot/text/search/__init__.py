import re
import os

max_found = 500

def search_in_files(file_list, pattern):
    pattern = '([<]p id[=]["]L([0-9]+)["] class[=]["]text["][>])' + '(.*' + pattern + ')'
    found_list = []
    print(pattern)
    for filepath in file_list:
        print(filepath)
        with open(filepath, encoding='utf8') as f:
            # print("file open success")
            text = f.read()
            # print(text)
            matches = re.findall(pattern, text)
            if matches:
                for m in matches:
                    if len(found_list) > max_found:
                        return found_list
                    found_list.append((filepath, m))
    return found_list
