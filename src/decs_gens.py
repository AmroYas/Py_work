
############################  Decorators ##########################
# Example:
import time
def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 =time.time()-t1
        print(f'{func.__name__} ran in {t2} seconds')
    return wrapper

@tictoc
def do_this():

    time.sleep(1.3)


@tictoc
def do_that():
    time.sleep(.4)

do_this()
do_that()
print('Done')


############################ Generators  ############################
# example:
def fetch_lines(filename):
    with open(filename, 'r') as file:
        lines = [] #remove
        for line in file:
            lines.append(line) #yield line
        return lines
zen = fetch_lines('C:/Users/islam/OneDrive/Desktop/vs_python/src/presentation/the_zen_of_python.txt')
print(zen)


def fetch_lines_again(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line
ben = fetch_lines_again('C:/Users/islam/OneDrive/Desktop/vs_python/src/presentation/the_zen_of_python.txt')
print(next(ben))


#############################  *args  #############################
# Example:
def order_pizza(size, *toppings):
    print (f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


order_pizza('large', 'peperoni','olives','sweetcorn','chicken')

###########################~ **kwargs  ############################
# Example:
def order_pizza(size, toppings, *details):
    print (f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print(f'\nDetails of the order are:')
    for key, value in details.items():
        print(f'- {key}: {value}')

order_pizza('large', 'peperoni','olives','chicken', delivery=True, tip=5)