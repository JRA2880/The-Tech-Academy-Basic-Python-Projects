
mySentence = 'loves the color'

colorList = ['red','blue','green','pink','teal','black']

def color_function(name):
    first = []
    i = 0
    for i in colorList:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        first.append(msg)
    return first

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Sally':
            print('Sally, you may not user this software!')
            
        else:
            go = False
    first = color_function(name)
    for i in first:
        print(i)

get_name()

