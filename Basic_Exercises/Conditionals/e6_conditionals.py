import random

weather = ['sunny', 'rainy', 'snowy', 'other']
selection = random.choice(weather)

match selection:
    case  'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case 'snowy':
        print("Want to build a snowman?")
    case 'other':
        print("Let's stay inside.")