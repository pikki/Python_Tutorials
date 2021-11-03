dict = {}
for i in range(1,11):
    if i%2 == 0 :
        dict[i] = 'even'
    else :
        dict[i] = 'odd'

#print(dict)

print({i:('even' if i%2 == 0 else 'odd') for i in range(1,11) })

# {append   if statement   else append   for loop}

