import numpy as np
import numpy.random as rnd

with open('event1.txt', 'w') as f:

    for t in range(2000):
        r=rnd.choice(range(10))
        if r<4:
            f.write( str(t)+ ' bronze\n')
        elif r<7:
            #print t, 'silver'
            f.write(str(t) + ' silver\n')
        elif r<8:
            #print t, 'gold'
            f.write(str(t) + ' gold\n')
