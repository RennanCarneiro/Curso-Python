#dictionary = a changeable, unordered collection of unique key: value pairs
# Fast cuz they use hashing, allow us to access a value quickly

capitals = {'Espanha' : 'Madrid',
            'Inglaterra' : 'Londres',
            'Brasil' : 'Brasília',
            'Italia' : 'Roma'}

#capitals.update({'Germany' : 'Berlin'})
#capitals.update({'Brasil' : 'Pernambuco'})
#capitals.pop('Espanha')
#capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany')) 
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key,value)
    