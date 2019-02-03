import json
import os
import webbrowser
import sys
import re


class MatcherUtil:
    url_regex = re.compile(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
                           re.IGNORECASE)
    file_path_regex = re.compile(r"^(/[^/ ]*)+/?$")

    @staticmethod
    def is_file_path(actual_hint):
        return re.match(MatcherUtil.file_path_regex, actual_hint)

    @staticmethod
    def is_hint_url(actual_hint):
        return re.match(MatcherUtil.url_regex, actual_hint)


class JSONUtil:
    #os.environ["HOME"] + "/local/share/devhints/hints.json"
    def __init__(self, json_file_path="../hints.json"):
        if ".json" in json_file_path:
            self.json_file_name = json_file_path
        else:
            print(f"{json_file_path} does not contain a JSON file.")
            exit(1)

    def open_hint(self, hint_key):
        data = self.read_json_from_file()
        actual_hint = data[hint_key]
        if MatcherUtil.is_hint_url(actual_hint):
            webbrowser.open_new(actual_hint)
        elif MatcherUtil.is_file_path(actual_hint):
            with open(actual_hint) as read_file:
                print(read_file.read())
        else:
            print(actual_hint)

    def write_to_json(self, data):
        if self.json_file_name:
            with open(self.json_file_name, "w") as write_file:
                json.dump(data, write_file)

    def read_json_from_file(self):
        if self.json_file_name:
            with open(self.json_file_name, "r") as read_file:
                try:
                    return json.load(read_file)
                except IOError:
                    print(f"devhints file does not exist")
        else:
            print(f"devhints file not set. use devhints. ")
        exit(1)


    # else:


if __name__ == "__main__":
    json_util = JSONUtil()
    args = sys.argv
    if len(args) >= 2:
        argname = args[1]
        if argname == "help":
            print("help")
        if argname == "add":
            print("add")
        if argname == "remove":
            print("remove")
        hint = argname
        json_util.open_hint(hint)