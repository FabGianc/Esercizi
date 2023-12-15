"""
prova di dizionari
"""

eng2it = dict()
print(eng2it)

eng2it={}
print(eng2it)

eng2it['one'] = 'uno'
eng2it['two'] = 'dos'
eng2it['two'] = 'due'

print(eng2it)

persona = {"nome":"Fabrizio", "cognome":"Giancola", "eta":"51", "località":"Faenza"}

print(persona)
print(len(persona))

if 'località' in persona:
    print(persona['località'])
    persona.pop('località')

print(persona)
print(persona.keys())
print(persona.values())

persona['paese'] = 'Italia'
print(persona)