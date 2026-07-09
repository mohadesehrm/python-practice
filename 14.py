names = input("نام کارکنان را وارد کنید: ")
k = int(input("عدد را وارد کن: "))
name = names.split()
cnt = len(name)
shift = name[cnt-k: ] + name[ :cnt-k]
print(shift)
