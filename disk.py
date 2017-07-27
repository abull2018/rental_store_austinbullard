import core
from core import car_price

def keep_history(car, days):
    price = core.car_price(car, days)

    message = ''
    if car == '1':
        car_type = 'Bugatti Veyron'
    elif car == '2':
        car_type = 'R.R Drophead Phantom Coupe'
    elif car == '3':
        car_type = 'Lambo Murcielago'
    elif car =='4':
        car_type = 'Ferrari F450'
    elif car == '5':
        car_type = 'Lambo Gallardo'
    
    message = '\n{}, {}, {}'.format(car, days, price)
    with open('history.txt', 'a') as file:
        file.write(message)

def write_log():
    cap = []
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        cap.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return cap

def in_stock():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left

def take_out(car_type, amount):
    str_l = ['car_type, in_stock, amount']
    left = in_stock()
    for item in left:
        if item[0] == car_type:
            if float(amount) > item[1]:
                print('We rented the last one out. Sorry for the inconvenience')
            else:
                item[1] = float(item[1]) - float(car)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)
    with open('inventory.txt', 'w') as file:
            file.write(message)

