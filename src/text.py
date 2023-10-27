# text manipulation

'spam eggs' 
"Paris rabbit got your back :)! Yay!"  
'1975'  # numbers can also be strings 

#-----------

'doesn\'t'  
"doesn't" 
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#--------------

s = 'First line.\nSecond line.'  # \n means newline
print(s)

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# --------------------------
# string concatination 
3 * 'un' + 'ium'
'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text

# 
prefix = 'Py'
#prefix 'thon'

prefix + 'thon'

#----------------------------
# strings indexing 

word = 'Python'
word[0]  # first character is at index 0
word[5]  

word[-1]  # returns last index 
word[-2]  # 2nd to the last
word[-6]

word[0:2] # index 2 excluded 
word[2:5] # index 5 excluded 

word[:2]  
word[4:] 
word[-2:]

word[:2] + word[2:]
word[:4] + word[4:]

word[42]

word[4:42]
word[42:]

# ---------

word[0] = 'J'
word[2:] = 'py'

'J' + word[1:]
word[:2] + 'py'

s = 'supercalifragilisticexpialidocious'
len(s)