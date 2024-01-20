##################################################
'''
Q1: 
'''

# TODO: Write your code here
for j in range(8):
    for i in range(j):
        print(i, end=" ")
    print()
##################################################
'''
Q2:
'''

# TODO: Write your code here
for j in range(1,8):
    for i in range(1,j):
        print(i, end=' ')
    print()
##################################################
'''
Q3:
'''

# TODO: Write your code here
for j in range(9,0,-1):
    for i in range(5):
        print(j, end='')
print()
##################################################
'''
Q4:
'''

# TODO: Write your code here
for j in range(9,0,-1):
    for i in range(j):
        print(j, end='')

print()
##################################################
'''
Q5:
'''

# TODO: Write your code here
for j in range(1,10,2):
    print('-' * (5-int(j/2)), end='')
    for i in range(j):
        print(j, end='')
    print()

##################################################
'''
Q6:
'''

# TODO: Write your code here
for i in range(1,6):
    print(' ' * (5-i+1), end='')
    for j in range(i):
        print(j+1, end='')
    for j in range(i-1,0,-1):
        print(j, end='')
    print()

##################################################
