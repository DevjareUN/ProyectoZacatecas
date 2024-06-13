import re

def camel_case_to_spaces(name):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', name).capitalize()


def snake_to_spaces(name: str):
    return name.replace("_", " ")

