from collections import OrderedDict # working with library
favourite_language = OrderedDict()
favourite_language['Utkarsh'] = 'python'
favourite_language['Shivam'] = 'java'
favourite_language['Robin'] = 'javascript'
for name,language in favourite_language.items():
    print(name.title() + "'s favourite language is " + language)