distance_mi = 7
is_restaurant_open = True
has_delivery_app = True
is_weather_bad = True
has_car = False

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if is_restaurant_open:
        print(True)
    else:
        print(False)
elif distance_mi <= 5:
    if is_restaurant_open and has_delivery_app:
        print(True)
    else:
        print(False)
else:
    if (has_car and not is_weather_bad) or has_delivery_app:
        print(True)
    else:
        print(False)
