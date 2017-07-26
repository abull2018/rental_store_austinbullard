def car_type(car):
    '''str -> str'''
    message = ''
    if car == '1' or car.lower() == 'one':
        car_type = 'Bugatti Veyron'
    elif car == '2' or car.lower() == 'two':
        car_type = 'R.R Drophead Phantom Coupe'
    elif car == '3' or car.lower() == 'three':
        car_type = 'Lambo Murcielago'
    elif car == '4' or car.lower() == 'four':
        car_type = 'Ferrari F450'
    elif car == '5' or car.lower() == 'five':
        car_type = 'Lambo Gallardo'
    return car_type 

def car_price(car, days):
    '''(str) -> float'''
    if car == '1':
        return float(days) * 40000
    elif car == '2':
        return float(days) * 3500
    elif car == '3':
        return float(days) * 2250
    elif car == '4':
        return float(days) * 1675
    elif car == '5':
        return float(days) * 1600




