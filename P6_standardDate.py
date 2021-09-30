import re,pyperclip
print('Hello Shiva baba my world')
#find dates in different format and store in standard format
# standard 2022-07-05

searchDate = re.compile(r'''(
    (\d{1,4})          # day or year
    (-|/)
    (10|11|12|0?[1-9])            # month
    (-|/)
    (\d{1,4})           # day or year
    )''',re.VERBOSE)

searchText = pyperclip.paste()
matchDate = searchDate.findall(searchText)
print(matchDate)

matches = []


for groups in matchDate:
    if len(groups[1])>2:
        stdDate = groups[1] + '-' + groups[3] + '-' + groups[5]
    else:
        stdDate = groups[5] + '-' + groups[3] + '-' + groups[1]
    matches.append(stdDate)

if len(matches)>0:
    print('\n'.join(matches))
    pyperclip.copy('\n'.join(matches))
else:
    print('no matches')

#remove multiple spaces
so= re.compile(r'\s{2,}')
mo = so.sub(' ','hello    ksdkja   asdkjssd')
print(mo)

# #remove multiple exclamation
# soo = re.compile(r'!{2,}')
# moo = soo.sub('!','hi!')
# print(moo)

#match , in numbers
# soo = re.compile(r'^\d{1,3}(,\d{3})*$')
# moo = soo.findall('1232 1 23 345 3,567 ')
# print(moo)
# for x in moo:
#     print(x)

#match firstname with Watnabae

# soo = re.compile(r'[A-Z][a-z]+\sWatan')
# moo = soo.findall('Mr. Watan sd Watan')
# print(moo)
text = ''''Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.''
'''

soo = re.compile(r'(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.I)
moo = soo.findall(text)
print(moo)





