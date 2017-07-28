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

# def find_car():




# def read_inventory(inventory):


