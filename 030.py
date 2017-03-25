people = 30
cars = 20
trucks = 15

if cars > people:
    print "We should take the cars."
elif cars < people and trucks < people:
    print "We could take the cars or trucks"
else:
    print "We can't decide."

if trucks > cars:
    print "That's too manu trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."   
