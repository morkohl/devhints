import json
import webbrowser

from matcher import MatcherUtil


class HintUtil:
    def __init__(self, json_file_path):
        self.json_file_name = json_file_path

    def list_hints(self):
        data = self.read_json_from_file()
        if len(data) > 0:
            print('{0:<20} {1:>5}'.format('HINT', 'VALUE'))
            for key in data:
                print('{0:<20} {1:>5}'.format(key, data.get(key)))
        else:
            print(f'{self.json_file_name} has no hints!')

    def remove_all_hints(self):
        self.write_to_json({})

    def remove_hint(self, hint_key):
        data = self.read_json_from_file()
        if not data.get(hint_key):
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
        try:
            actual_hint = data[hint_key]
        except KeyError:
            print("Key does not exist")
            exit(1)

        if MatcherUtil.is_url(actual_hint):
            webbrowser.open_new(actual_hint)
        elif MatcherUtil.is_file_path(actual_hint):
            with open(actual_hint) as read_file:
                print(read_file.read())
        else:
            print(actual_hint)

    def write_to_json(self, data):
        try:
            with open(self.json_file_name, "w") as write_file:
                json.dump(data, write_file)
        except IOError as err:
            print(f"Encountered error when reading from file {self.json_file_name}; {err}")
            exit(1)

    def read_json_from_file(self):
        try:
            with open(self.json_file_name, "r") as read_file:
                return json.load(read_file)
        except Exception as err:
            print(f"Encountered error when reading from file {self.json_file_name}; {err}")
            exit(1)