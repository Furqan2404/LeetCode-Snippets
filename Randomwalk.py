
import random                                       ##Author: Furqan2404

def randomwalk(n):
    x=0
    y=0

    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step=='N':
            y+=1
        elif step == 's':
            y-=1
        elif step == 'E':
            x+=1
        elif step =='W':
            x-=1
    return (x,y)

def RandomWalktwo(n):
    x,y = 0,0 ##inititalizing x and y
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x+=dx
        y+=dy
    return (x,y)


##what is the longest walk that you can take to end up 4 or less blocks from home

num_of_walks = 20000

for walk_len in range(1,31):
    no_transport = 0  ##track blocks or fewer from home
    for i in range(num_of_walks):
        (x,y) = RandomWalktwo(walk_len)
        distance = abs(x) + abs(y)
        if distance <=4:
            no_transport+=1
    no_transport_per =  float(no_transport)  / num_of_walks

    print("Walk size = ", walk_len, "/ % of no transport=", 100 * no_transport_per)


