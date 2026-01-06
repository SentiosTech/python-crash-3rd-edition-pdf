def make_car(manufacture,model, **car_info):
    car_info['manufacture'] = manufacture
    car_info['model'] = model
    return car_info

car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)