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

# def r_value(car):
#     '''str -> str'''
#     message = ''
#     if car == '1' or car.lower() == 'one':
#         r_value = '1300000'
#     elif car == '2' or car.lower() == 'two':
#         r_value = '450000'
#     elif car == '3' or car.lower() == 'three':
#         r_value = '250000'
#     elif car == '4' or car.lower() == 'four':
#         r_value = '210000'
#     elif car == '5' or car.lower() == 'five':
#         r_value = '200000'
#     return r_value 

def car_price(car, days):
    '''(str) -> float'''
    if car == '1':
        price = float(days) * 40000
        sales_tax = 0.07
        tax = price * sales_tax
        total_price = price + tax
        return total_price
    elif car == '2':
        price = float(days) * 3500
        sales_tax = 0.07
        tax = price * sales_tax
        total_price = price + tax
        return total_price
    elif car == '3':
        price = float(days) * 2250
        sales_tax = 0.07
        tax = price * sales_tax
        total_price = price + tax
        return total_price 
    elif car == '4':
        price = float(days) * 1675
        sales_tax = 0.07
        tax = price * sales_tax
        total_price = price + tax
        return total_price
    elif car == '5':
        price = float(days) * 1600
        sales_tax = 0.07
        tax = price * sales_tax
        total_price = price + tax
        return total_price 


