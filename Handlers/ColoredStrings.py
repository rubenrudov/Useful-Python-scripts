"""
Author: Ruben Rudov
Date: 29/06/2021
Purpose: basic class for coloring strings while printing
@TODO: Add more colors
"""


class Colors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL_MARKER = '\033[101m'

    @classmethod
    def print_options(cls):
        print("Basic class for coloring strings in log")

    def __str__(self):
        return "String coloring class"
