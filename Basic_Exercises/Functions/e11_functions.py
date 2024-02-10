def greet(language_code):
    if language_code == 'en':
            return 'Hi!'
    elif language_code == 'fr':
            return 'Salut!'
    elif language_code == 'pt':
            return 'Olá!'
    elif language_code == 'de':
            return 'Hallo!'
    elif language_code == 'sv':
            return 'Hej!'
    elif language_code == 'af':
            return 'Haai!'
            
def extract_language(language):
    return language[:2]
    
def extract_region(region):
    return region[3:5]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    
    if language == 'en' and region == 'US':
        return 'Hey'
    elif language == 'en' and region == 'GB':
        return 'Hello'
    elif language == 'en' and region == 'AU':
        return 'Howdy!'
    else:
        return greet(language)
        
print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!



print(local_greet('en_US.UTF-8'))    # US
print(local_greet('en_GB.UTF-8'))    # GB
print(local_greet('af_AF.UTF-16'))   # KR