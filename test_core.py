import core

def test_car_type():
    assert core.car_type('1') == 'Bugatti Veyron'
    assert core.car_type('2') == 'R.R Drophead Phantom Coupe'
    assert core.car_type('3') == 'Lambo Murcielago'
    assert core.car_type('4') == 'Ferrari F450'
    assert core.car_type('5') == 'Lambo Gallardo'
    assert core.car_type('one') == 'Bugatti Veyron'
    assert core.car_type('two') == 'R.R Drophead Phantom Coupe'
    assert core.car_type('three') == 'Lambo Murcielago'
    assert core.car_type('four') == 'Ferrari F450'
    assert core.car_type('five') == 'Lambo Gallardo'
    

def test_car_price():
    assert core.car_price('1', 2) == 80000
    assert core.car_price('2', 4) == 14000
    assert core.car_price('3', 6) == 13500
    assert core.car_price('4', 8) == 13400
    assert core.car_price('5', 10) == 16000
    
