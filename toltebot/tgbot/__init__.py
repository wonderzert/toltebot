# -*- coding: utf-8 -*-

from . import text
import json
import os
import urllib
import requests

def search(query):
    search_results = text.search.search_in_files(text.filelist.file_list, query)
    processed_results = []
    for s in search_results:
        filepath, match = s
        filepath = os.path.relpath(filepath, text.filelist.textpath)
        # print(match)
        linenum = match[1]
        match_text = match[2]

        link_template = \
            '<a href="' + \
            "https://nagualchat.github.io/" + \
            urllib.parse.quote(filepath) + "#L" + linenum + \
            '">' + os.path.basename(filepath) + '</a>'

        tgresult_obj = {
            "type": "article",
            "id": filepath[0:32] + linenum,
            "title": os.path.basename(filepath),
            "description": match_text,
            "input_message_content": {
                "message_text": link_template + ': ' + match_text,
                "parse_mode": "html"
            }
        }

        processed_results.append(tgresult_obj)
    return processed_results

def handle_update(update):
    # print(update)
    update = json.loads(update, encoding="utf8")
    # print("handling update")
    # print(update)
    # try:
    query = update['inline_query']['query']
    offset = 0
    try:
        offset = int(update['inline_query']['offset'])
    except Exception:
        pass
    search_result = search(query)
    search_result = search_result[offset:5]
    answer_command = {
        "method": "answerInlineQuery",
        "inline_query_id": update['inline_query']['id'],
        "results": json.dumps(search_result),
        "next_offset": offset + 5
    }
    r = requests.post( \
    "https://api.telegram.org/bot403483963:AAFDfy0wV3oq7mpYwCE51EKU7bVbyWjIVsk/" \
    + answer_command["method"], answer_command)
    # print(answer_command)
    # print(r.text)
    return json.dumps(answer_command)
    # except Exception:
        # print("exception")
        # pass
    return None
