fisrt_name = input("نام: ")
last_name = input("نام خانوادگی: ")
year = int(input("سال تولد: "))
passw = fisrt_name[ :3] + last_name[ :2] + str(year)
print(passw.lower())

