# dictionary =  A changeable, unordered collection of unique key:value pairs.
#               Fast because they use hashing, allowing for O(1) retrieval.

capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Italy': 'Rome'}

print(capitals)
print(capitals['USA'])
capitals['Spain'] = 'Madrid'

print(capitals)
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany': 'Berlin'})
capitals.pop('France')
capitals.clear()


for key, value in capitals.items():
    print(key, value)