dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1) # copy of the object, it is a new object
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# because dict2 is a new object, the change to dict2 does not affect dict1
# the printout should be The Life of Brian