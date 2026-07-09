def check(password):
    if len(password) <= 8:
        return "Invalid"
    f1 = False
    f2 = False
    f3 = True
    for char in password:
        if '0' <= char <= '9':
            f1 = True
        elif 'A' <= char <= 'Z':
            f2 = True
        else:
            f3 = False
    if not f1:
        return "Invalid"
    if not f2:
        return "Invalid"
    if f3 and len(password) > 0 :
        return "Invalid"
    return "Valid"
print(check(input("رمز عبور خود را وارد کنید: ")))