
# polymorpshime


mylist = [1, 2, 3, 4, 5]
msg = 'Hello, OOP'
dict = {'name':'Fair','age':21,'major':'MIT' }

print(len(mylist))
print(len(msg))
print(len(dict))


def introduce(name):
    print(f'My name is {name}')

def introduce(name,age):
    print(f'My name is {name},i am {age} year old.')

introduce('Fair')
introduce('Ton',37)