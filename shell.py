import core
import disk
# print('Hello World')

def main():
    msg = '''Welcome to L\'s Garage!! Here is what we have to offer!!
    \t1. Bugatti Veyron.$40000\n
    \t2. R.R Drophead Phantom Coupe.$3500\n
    \t3. Lambo Murcielago.$2250\n
    \t4. Ferrari F450.$1675\n
    \t5. Lambo Gallardo.$1600\n
    '''
    while True:
        car = input(msg)
        if car == '1' or car == '2' or car == '3' or car == '4' or car == '5':
            break
        else:
            print('Sorry, Invalid choice!')
    days = input('How many days would you like to rent this car?\n')
    print('Your total will be ${:.2F}'.format(core.car_price(car, days)))

    car_type = disk.keep_history(car, days)
    disk.take_out(car, days)
    print('Thank you!\n!!!Warning!!!\nWe are not responsible for any speeding tickets!!!\nAny damage to the vehicle with be added to the bill!')
    
if __name__ == '__main__':
    main()

