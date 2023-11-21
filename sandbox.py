import re

counter = {}

def renumber(match):
    v = match.group(1)
    if v in counter.keys():
        counter[v] += 1
    else:
        counter[v] = 1
    return '{' + match.group(1) + str(counter[v]) + '}'

story_text = '''Once upon a time in a long-ago {place}, there lived a large {adjective} and {adjective} and {adjective} {noun}. It loved to {verb} {plural_noun}'''
# story_text = '''Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}'''
modified_text = re.sub(r'\{(.*?)\}', renumber, story_text)
variables = re.findall(r'\{(.*?)\}', modified_text)
print(variables)
print(modified_text)
