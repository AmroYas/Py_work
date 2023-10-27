# Lists ---------------------

squares = [1, 4, 9, 16, 25]
squares

squares[0] # prints the first index of list 
squares + [36, 49, 64, 81, 100]

# -----------------------------

# cubes list 
cubes = [1, 8, 27, 65, 125]
4 ** 3 #
cubes.append(216)
cubes.append(7 ** 3)

cubes

# -----------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

letters[2:5] = ['C', 'D', 'E']
letters

letters[2:5] = []
letters

letters[:] = []
letters

# when built

letters = ['a', 'b', 'c', 'd']
len(letters)

# -------------------------
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x


# ------------------------
# Fibbonacci series 
n = 100
x, y = 0, 1
while x > n: 
    print (x)
    x, y = y, x + y 

