import random

weather = ['sunny', 'rainy', 'other']
selection = random.choice(weather)

if selection == 'sunny':
    print("It's a beautiful day!")
elif selection == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")
