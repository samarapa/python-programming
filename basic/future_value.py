def future_value():
    amt = 10000
    inrt = 3.5
    yrs = 7

    future_value = amt * ( 1+ (0.01*inrt)) ** yrs
    return round(future_value,2)

print(future_value())
