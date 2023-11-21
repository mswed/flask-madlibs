import json

f = {
    'original': {'words': ["place", "noun", "verb", "adjective", "plural_noun"],
                 'text': """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}.
                  It loved to {verb} {plural_noun}."""},
    'vacation': {'words': ['adjective', 'adjective2', 'noun', 'noun2', 'plural_noun', 'game', 'plural_noun2',
                           'verb_ending_in_ing', 'verb_ending_in_ing2', 'plural_noun3', 'verb_ending_in_ing3',
                           'noun3', 'plant', 'body_part', 'place', 'verb_ending_in_ing4', 'adjective3', 'number',
                           'plural_noun4'],
                 'text': """ A vacation is when you take a trip to some {adjective} place with your {adjective2} family.
                 Usually you go to some place that is near a/an {noun} or up on a/an {noun2}. A good vacation place
                 is one where you can ride {plural_noun} or play {game} or go hunting for {plural_noun2}. I like
                 to spend my time {verb_ending_in_ing} or {verb_ending_in_ing2}. When parents go on a vacations,
                 they spend their time eating three {plural_noun3} a day, and fathers play golf, and mothers
                 sit around {verb_ending_in_ing3}. Last summer, my little brother fell in a/an {noun3} and
                 got poison {plant} all over his {body_part}. My family is going to go to (the){place} and I will
                 practice {verb_ending_in_ing4}. Parents need vacation more than kids because parents are always
                 very {adjective3} and because they have to work {number} hours every day all year making enough
                 {plural_noun4} to pay for the vacation."""}
}
with open('stories.json', 'w') as output:
    json.dump(f, output)

stories = json.load('stories.json')