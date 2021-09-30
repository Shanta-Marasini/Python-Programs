import random
print('Hello Shiva baba my world')

def rollDice():
    number = random.randint(1,6)
    u = ['   ','   ','   ']
    m = ['   ','   ','   ']
    l = ['   ','   ','   ']

    if number == 1:
        m[1] = '0'
        print('----------')
        print(' '.join(u))
        print(' '.join(m))
        print(' '.join(l))
        print('----------')

    if number == 2:
        m[0] = m[2] = ' 0'
        print('----------')
        print(' '.join(u))
        print(' '.join(m))
        print(' '.join(l))
        print('----------')

    if number == 3:
        m[1] = u[1] = l[1] = '0'
        print('----------')
        print(' '.join(u))
        print(' '.join(m))
        print(' '.join(l))
        print('----------')

    if number == 4:
        u[0] = l[0] = ' 0'
        u[2] = l[2] = '0'
        print('----------')
        print(' '.join(u))
        print(' '.join(m))
        print(' '.join(l))
        print('----------')

    if number == 5:
        u[0] = l[0] = ' 0'
        u[2] = l[2] = m[1] = '0'
        print('----------')
        print(' '.join(u))
        print(' '.join(m))
        print(' '.join(l))
        print('----------')

    if number == 6:
        u[0] = m[0] = l[0] = ' 0'
        u[2] = l[2] = m[2] = '0'
        print('----------')
        print(' '.join(u))
        print(' '.join(m))
        print(' '.join(l))
        print('----------')



print('This is a dice simulator.')
while True:
    player = input('Press y to roll:')
    if player == 'y':
        rollDice()
    else:
        break