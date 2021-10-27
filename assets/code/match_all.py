import random

names = [ 'Hannah Chay', 'Teddy Fujimoto', 'Enrique Gomez Gomez', 'Akshay Govindan', 'Chris Hemauer', 'Caroline Henry', 'Chase Hubbart', 'Nana Kusi', 'Nistha Panda', 'Kenneth Peng', 'Alexandra Sacco', 'Russell Scharf', 'Charles Shen', 'Gary Twu' ]

random.shuffle( names )

n_names = len(names)
width = max( [ len(x) for x in names ] )
for i in range(0, n_names, 2):
    print('Pair:', names[i].rjust(width), '+', names[i+1].ljust(width) )

