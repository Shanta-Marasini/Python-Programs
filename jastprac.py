print('Hello my world')

w = len('{0:b}'.format(17))
for i in range(1,18):

    print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=w))
