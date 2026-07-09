def check(number):
    flag = False
    if number == 2:
        flag = False
    elif number > 2:
        for i in range(2,number-1):
            if number%i==0:
                flag = True
    else:
       flag = True
    if flag:
        return "اول نیست"
    else:
        return "اول است"
print(check(int(input("عدد مورد نظر خود را وارد کنید: "))))