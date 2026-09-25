hours_available = 3
library_open = True
has_laptop = True
has_charger = False
can_borrow_charger = True

if not hours_available:
    print(False)
elif hours_available <= 1:
    if library_open:
        print(True)
    else:
        print(False)
elif hours_available <= 4:
    if library_open and has_laptop:
        print(True)
    else:
        print(False)
else:
    if library_open and has_laptop and (has_charger or can_borrow_charger):
        print(True)
    else:
        print(False)
