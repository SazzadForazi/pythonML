# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(myCat["size"])
# print(myCat.keys())
# print(myCat.items())


from itertools import count


message = 'It was a bright cold day in April, and the clocks were striking'
count = {}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1

print(count)
