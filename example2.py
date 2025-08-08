v = 200 
w = 540
if (w & 1) == 1 or w < 2 or w <= v :
    print ("Invalid input")
else: 
    x = ((4*v) - w)//2
    print ("Two wheeler = {0} Four Wheeler = {1}".format(x,v-x))