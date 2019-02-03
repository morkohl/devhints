import re as regex


class MatcherUtil:
    url_regex = regex.compile(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
                              regex.IGNORECASE)
    file_path_regex = regex.compile(r"^(/[^/ ]*)+/?$")

    @staticmethod
    def is_file_path(actual_hint):
        return regex.match(MatcherUtil.file_path_regex, actual_hint)

    @staticmethod
    def is_hint_url(actual_hint):
        return regex.match(MatcherUtil.url_regex, actual_hint)