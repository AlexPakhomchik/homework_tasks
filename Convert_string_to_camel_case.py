# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
# often referred to as Pascal case). The next words should be always capitalized.

def to_camel_case(text):
    if '-' in text or '_' in text:
        find_split = text.replace('_', '-')
        print(find_split)
        list_text = find_split.split('-')
        print(list_text)
        new_text = ''
        for i in list_text:
            if i != list_text[0] and i != '':
                new_text += i[0].upper() + i[1:]
            else:
                new_text += i
        print(new_text)
        return new_text
    elif text == '':
        return text
