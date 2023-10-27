
# 4.1 If statements

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# 4.2 for statement ------------------------------

# loop over collection 
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# loop over a copy of collection 

users = {'Hans': 'active', 
         'Éléonore': 'inactive', 
         '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# loop oer a new collectio

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# 4.3 The range function -------------------

# loop generating arithmatic progressions
for i in range(5):
    print(i)

# range can start at other set of nums
list(range(5, 10))
list(range(0, 10, 3)) # increments at 3
list(range(-10, -100, -30)) # negative steps 

# iterate over indicies of a sequence 
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i]) # index of a

# will not generate a range 
range(10)

sum(range(4)) # sums numbers from 0 to 3

# 4.4 break and contrinue statements 

# for loop to search for prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0: # if n is even
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0: # if n is even
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue statament 
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# 4.5 pass statement ------------------------

# has no action 
while True:
    pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass

# 4.6 

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
            #case 401 | 403 | 404:
            #return "Not allowed"

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

# names constants in patterns 

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

##

def retail_shop(type, *arg, **key):
    print(" I am looking for", kind)
    print(" sory we are out of", kind)
    for ag in arg:
        print(arg)

