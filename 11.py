def price(distance):
    if distance<=3:
        return 15000
    elif 3<distance<=10:
        return distance*4000
    else:
        return distance*3000
print(price(int(input("فاصله مبدا تا مقصد به کیلومتر چقدر است؟ "))))