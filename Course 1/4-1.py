def greet(lang):
    if lang =='es':
        print('hola')
    elif lang == 'fr':
        return 'bonjour'
    else:
        print('hello')
greet('en')
greet('es')
print(greet('fr'),'Sally')

def gr():
    return "hello"
print(gr(),'glenn')

def func(x) :
    print(x)

func(10)
func(20)

def stuff():
    print('Hello')
    return
    print('World')

stuff()

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
