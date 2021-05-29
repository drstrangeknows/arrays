'''
Simple concept is if you don't have enough petrol compared to the distance that you have
to travel, then you can't reach next destination. Take a counter variable i.e. tank and fill
it up at every junction. Compare the distance(to the next junction) to the tank fuel. If you
have fuel left for next junction, then use the fuel to go next junction(deduct fuel equal to dist)
if you don't have enough fuel, that means the index you started with is not right. In that case,
empty fuel tank, and set start to next junction from the current index. At this point, start 
calculating the shortage from every junction where you don't have enough fuel in tank to go to next
station. After scanning entire array, if there is fuel in tank to account for shortage, that shows
you can traverse all stations and you can pick the station as start from where you reached the end station
and had enough fuel in tank to cover the shortage. The idea is to find the junction from where we can 
reach till last junction plus we should have enough fuel to cover up the shortage that was added at
every junction where we could not reach next station
'''

def find_start(gas, cost):

    tank = 0
    shortage = 0
    start = 0

    for ind in range(len(gas)):
        tank+=gas[ind]

        if tank>=cost[ind]:
            tank-=cost[ind]
        else:
            shortage+=cost[ind]-tank
            start=ind+1
            tank=0
    
    if start == len(gas) or tank<shortage:
        return -1
    else:
        return start

########################### Alternate soution ######################

    # start = 0
    # curTank = 0
    # totTank = 0

    # for i in range(len(gas)):
    #     curTank += gas[i] - cost[i]
    #     totTank += gas[i] - cost[i]

    #     if curTank < 0:
    #         start = i+1
    #         curTank = 0

    # return -1 if (totTank<0) else start
##############################

def main():
    gas_arr = [5,1,2,3,4]
    cost_arr = [4,4,1,5,1]

    pos = find_start(gas_arr, cost_arr)

    if pos==-1:
        print("No station feasible")
    else:
        print("start at {0} station".format(pos))

if __name__=='__main__':
    main()