import json,time
from difflib import get_close_matches
print('Hello Shiva baba my world')


data = json.load(open('original.json'))
actualAns = ''

while True:
    word = input('Enter the word you want to search: ')
    actualWord = word.lower()
    if actualWord == 'q':
        break
    elif actualWord in data:
        actualAns = data[actualWord]
    elif actualWord.upper() in data:
        actualAns = data[actualWord.upper()]
    elif actualWord.title() in data:
        actualAns = data[actualWord.title()]
    elif len(get_close_matches(actualWord,data.keys())) > 0:
        matchAns = get_close_matches(actualWord,data.keys())[0]
        print(f'did you mean "{matchAns}" instead?: ')
        decide = input('enter y for yes n for no: ')
        if decide == 'y':
            actualAns = data[matchAns]
        elif decide == 'n':
            actualAns = 'We dont have that word?Would you like to try again'
        else:
            actualAns = 'Sorry not found'

    else:
        print('sorry not found')

    if type(actualAns)== list:
        j = 1
        for i in actualAns:
            print(f'{j}. {i}')
            j += 1
    else:
        print(actualAns)

    print('')
    time.sleep(0.5)



    # if actualWord == 'q':
    #     break
    # ansL = data.get(actualWord,'no')
    # ansU = data.get(actualWord.upper(),'no')
    # ansT = data.get(actualWord.title(), 'no')
    # ansList = [ansL,ansU,ansT]
    # for i in ansList:
    #     if i != 'no':
    #         actualAns = i
    #         break
    #     else:
    #         actualAns = 'Sorry the word doesnot exist here'


