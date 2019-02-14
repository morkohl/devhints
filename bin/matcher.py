import re as regex


class MatcherUtil:
    url_regex = regex.compile(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
                              regex.IGNORECASE)
    file_path_regex = regex.compile(r"^((\.{1,2})?\/[^\/ ]*)+?$")

    @staticmethod
    def is_file_path(actual_hint):
        return regex.match(MatcherUtil.file_path_regex, actual_hint)

    @staticmethod
    def is_url(actual_hint):
        return regex.match(MatcherUtil.url_regex, actual_hint)

    @staticmethod
    def is_json_file(actual_hint):
        return (MatcherUtil.is_file_path(actual_hint) and regex.match(r".*\.json", actual_hint)) or regex.match(r".*\.json", actual_hint)