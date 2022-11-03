import random

hero=[ "mark", "sam"]
verbs=[ "helped", "play", "lie", "replace", "drink", "exist"]
noun= [ "playground", "school", "train", "helicopter", "notebook", "dog"]

def hero2 (words_from_data):
    if  "<heros>" in words_from_data:
        words_from_data = words_from_data.replace("<heros>",(random.choice(hero)).capitalize())
    return words_from_data
def verb1 (happy):
    if "<verbs>" in happy: 
        happy = happy.replace("<verbs>",(random.choice(verbs)).capitalize())
    return happy
def nounreplace (light):
    if "<nouns>" in light:
        light = light.replace("<nouns>",(random.choice(noun)).capitalize())
    return light.capitalize()
for i in range(2):
    lines = list()
    with open('story.txt') as f:
        lines = f.read()
        fixed = hero2(verb1(nounreplace(lines)))
    print(fixed)

