import json
import webbrowser

from matcher import MatcherUtil


class HintUtil:

    def __init__(self, json_file_path="../hints.json"):
        if ".json" in json_file_path:
            self.json_file_name = json_file_path
        else:
            print(f"{json_file_path} does not contain a JSON file.")
            exit(1)

    def list_hints(self):
        print("listing all k/v's\n")
        data = self.read_json_from_file()
        for kv in data:
            print(kv, data.get(kv))

    def remove_all_hints(self):
        self.write_to_json({})

    def remove_hint(self, hint_key):
        data = self.read_json_from_file()
        if data.get(hint_key):
            print("Key is not set!")
            exit(1)
        data = list(filter(lambda key, value: key != hint_key, data))
        self.write_to_json(data)
        return data

    def add_hint(self, hint_key, file_path):
        data = self.read_json_from_file()
        if data.get(hint_key):
            print("Key already used. Remove it first to replace it!")
            exit(1)
        data[hint_key] = file_path
        self.write_to_json(data)
        return data

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