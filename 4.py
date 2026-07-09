numbers = []
while True:
    num = input("شماره را وارد کنید: ")
    if num == "0":
        break
    else:
        numbers.append(num)
r_num = numbers[ : :-1]
for i in r_num:
    print(i)