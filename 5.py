n = int(input("وارد کنید: "))
for i in range (1,n+1):
    for x in range(1,n+1):
        print(i*x , end=" ")
        if x == 5:
            print(f'\n')