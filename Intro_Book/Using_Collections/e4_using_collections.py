pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets['Lizard'] if pets.get('lizard') != None else None)
print(pets['Lizard'] if pets.get('lizard') != None else '<silence>')

#or

print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>' )