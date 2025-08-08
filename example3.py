N = 10
K = 5

jar = N

def sell(order):
    global jar
    if order <= 0 or order > jar :
        print ("INVALID INPUT")
        print (f"NUMBER OF CANDIES LEFT:{jar}")
        return
    
    jar -= order
    print (f"NUMBER OF CANDIES SOLD: {order}")
    print (f"NUMBER OF CANDIES LEFT: {jar}")

'''if jar <= K:
    jar = N
    print ("JAR IS REFILLED TO FULL (10 CANDIES)")
'''

while True:
    try:
        user_input = int(input("Enter number of candies to buy (o to exit):"))
        if user_input == 0:
            print ("INVALID INPUT")
            print (f"NUMBER OF CANDiES LEFT: {jar}")
            break
        sell (user_input)

        if jar <= K :
            jar = N
            print ("JAR IS REFILLED TO FULL (10 CANDIES)")
    except ValueError:
        print ("Please enter a valid integer.")