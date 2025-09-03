'''JavaScript Object Notation'''
import json

with open('states.json') as f:
    data = json.load(f)

abb_mapping = dict()

for state in data['states']:
    state_name = state['name']
    state_abbrv = state['abbreviation']
    abb_mapping[state_abbrv] = state_name

print(abb_mapping['PA'])

#for state in data['states']:
#    del state['area_codes']

#with open('test_states.json', 'w') as f:
#    json.dump(data, f, indent=2)