glossary = {
    'Dictionary': 'A collection of key-value pairs.',
    'Key-Value Pair': 'A set of values associated with each other.',
    'Conditional Test': 'An expression that can be evaluated as True or False.',
    'List': 'A collection of items in a particular order.',
    'Syntax Error': 'When a programming language does not recognise a section of your program as valid code.',
    'Set': 'A collection in which each item must be unique',
    'pop()': 'A method that removes the last item in a list, but lets you work with that item after removing it.',
    'append()': 'A method that adds a new element to the end of a list',
    'Index': 'The position of an element in a list of values; typically starts at 0.',
    'Constant': 'A variable whose value stays the same throughout the life of a program.'
}

for term, definition in glossary.items():
    print(f"\n{term}:")
    print(f"\t{definition}")