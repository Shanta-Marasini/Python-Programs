import re,pyperclip
#finding URLS i.e starting with http:// or https://

searchHttp = re.compile(r'''(
    https?://
    (w{3}\.)?  
    [a-zA-Z0-9_~.-]+
    (\.[a-zA-Z]+)
    )''',re.VERBOSE)

searchText = pyperclip.paste()
matchHttp = searchHttp.findall(searchText)
matches = []
for groups in matchHttp:
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print(f'there are {len(matches)} URLS in this page: ')
    for x in matches:
        print(x)
else:
    print('no matches')






