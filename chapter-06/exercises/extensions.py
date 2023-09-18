favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favourite language is {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language.title()}")