fisrt_names = input("نام خانوادگی دانش آموزان را وارد کنید: ")
fisrt_name = fisrt_names.split()
last_names = input("نام دانش آموزان را وارد کنید: ")
last_name = last_names.split()
for i in fisrt_name:
    for x in last_name:
        print(i , x)
