import core
import disk
from core import car_price
import sys, time

typing_speed = 13
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()




# print('Hello World')

def main():
    msg = '''🚗\nWelcome to L\'s Garage 🕴 🕴 🖐\nHere is what we have to offer ‼\n🏎
    ╔                                         ╗
    ├What would you like to drive away today⁈ ┤\n
    ╏\t1. Bugatti Veyron╌💲40000             ╏\n            
    ╏\t2. R.R Drophead Phantom Coupe╌💲3500  ╏\n 
    ╏\t3. Lambo Murcielago╌💲2250            ╏\n           
    ╏\t4. Ferrari F450╌💲1675                ╏\n
    ╏\t5. Lambo Gallardo╌💲1600              ╏\n
    ╚                                         ╝
    '''
    while True:
        car = slow_type(msg)
        if car == '1' or car == '2' or car == '3' or car == '4' or car == '5':
            break
        else:
            print('🚫 Sorry, Invalid choice🕴 🚫')
    days = slow_type('« ℋ ow many days would you like to rent this car⁈ »\n')
    print('Your total will be 💲{:.2F}'.format(core.car_price(car, days)))

    car_type = disk.keep_history(car, days)
    disk.take_out(car, days)
    # disk.add_back(car, days)
    print('Thank you!\n')
    print("⚠"'\nWe are not responsible for any tickets ‼\n'"⚠")

if __name__ == '__main__':
    main()


