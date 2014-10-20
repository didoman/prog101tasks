# calculate coins

def calculate_coins(money):
    coinsset = [100,50,20,10,5,2,1]
    money = int(money*100)

    answerset = {}
    counter = 0

    while money != 0:
        if money - coinsset[counter] >=0:
            money = money - coinsset[counter]
            if coinsset[counter] not in answerset.keys():
                answerset[coinsset[counter]] = 1
            else:
                answerset[coinsset[counter]] += 1
        else:
            counter += 1

    print (answerset)

calculate_coins(0.33)
calculate_coins(0.53)
calculate_coins(1.33)
calculate_coins(4.63)

