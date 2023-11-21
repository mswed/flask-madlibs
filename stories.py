import json
import os

"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, name, words, text):
        """Create story with words and template text."""

        self.name = name
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

    def save(self):
        """Save the story in JSON format"""
        if os.path.isfile('stories.json'):
            with open('stories.json', 'r') as input_file:
                stories = json.load(input_file)
        else:
            stories = {}

        stories[self.name] = {'words': self.prompts, 'text': self.template}
        with open('stories.json', 'w') as output:
            json.dump(stories, output)



# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )
