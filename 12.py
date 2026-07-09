a,b = map(int,input("دو عدد مورد نظر را وارد کنید: ").split())
x = input("عملگر مورد نظر را از بین + - * / انتخاب کنید: ")
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if x == "+":
    print(sum(a,b))
elif x == "-":
    print(sub(a,b))
elif x == "*":
    print(mul(a,b))
elif x == "/":
    print(div(a,b))

