
def create_list( y ):
    numbers = []
    i = 0
    while i < y :
        #print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        #print "Numbers now: ", numbers
        #print "At the bottom i is %d" % i
    return numbers

numbers = create_list(6)

print "The numbers finally : ", numbers

#for num in numbers:
#    print num
