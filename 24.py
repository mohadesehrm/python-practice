a = int(input("عدد مورد نظر خود را وارد کنید: "))
ma = []
for i in range(2 , a-1):
    if a%i==0:
        ma.append(i)
cnt = len(ma)
flag = False
if cnt == 2:
    flag = False
elif cnt > 2:
    for i in range(2,cnt-1):
        if cnt%i==0:
            flag = True
        else:
            flag = True
if flag:
    print("جادویی نیست")
else:
    print("جادویی است")