# 4.7 Functions

# a function for the Fibonacci series

def fib(n):
    a,b = 0, 1
    while a < n:
        print(a, end = ' ')
        a,b = b, a+b
    print()

fib(50)

# returnin the result as a list

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100

# 4.8 More on functions ------------------------

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# value taken from the defining scope
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# however, function can accumlate values too
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# to prevent accumeation 
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# using keyword args in functions

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# function fails due to resrictions 
def function(a):
    pass
function(0, a=0)

# function for a tuple 

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# using / and * markers in functions 

def standard_arg(arg): # most common
    print(arg)

# restricted to only use positional parameters 
def pos_only_arg(arg, /): 
    print(arg)

# only allows keyword arguments
def kwd_only_arg(*, arg):
    print(arg)

# no arg, either, arg
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


def foo(name, **kwds):
    return 'name' in kwds

def foo(name, /, **kwds):
    return 'name' in kwds

#foo(1, **{'name': 2})

def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})

# -------------------

def concat(*args, sep="/"):
    return sep.join(args)

# concat("earth", "mars", "venus")

# concat("earth", "mars", "venus", sep=".")

#-------------------

list(range(3, 6))            # normal call with separate arguments

args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list

# ---------------------
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# -------------------------

# Lambda expressions 

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)

# ---------------------

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

#------------------------

# multi line docstring 
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# -----------------------------

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')