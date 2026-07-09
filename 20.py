word = input("کلمه مورد نظر خود را وارد کنید: ")
wordr = word[::-1]
if wordr == word:
    print("yes")
else:
    print("no")