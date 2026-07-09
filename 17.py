scores = list(map(int,input("نمرات را وارد کنید: ").split()))
maxx = max(scores)
print(f"بیشترین : {maxx}")
av = (sum(scores)/len(scores))
print(f"میانگین : {av}")
if len(scores)%2==0:
    m = int(len(scores)/2)
    print(f" میانه = {scores[m],scores[m-1]}")
else:
    m = int(len(scores)/2)
    print(f"میانه = {scores[m]}")
