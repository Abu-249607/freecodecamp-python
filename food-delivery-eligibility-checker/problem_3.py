distance_mi = 12
is_raining = False
has_bike = True
has_car = False
has_ride_share = True
has_train_access = False

if not distance_mi:
    print(False)

elif distance_mi <= 2:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 8:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 20:
    if has_car or has_ride_share:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share or has_train_access:
        print(True)
    else:
        print(False)
