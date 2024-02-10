def contains(city, places):
    for place in places:
        if place == city:
            return True
    
    return False

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']
                


print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))