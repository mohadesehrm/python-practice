numbers = list(map(int,input("enter: ").split()))
s_num = sorted(numbers , reverse= False)
n_num = sorted(numbers , reverse=True)
if numbers == s_num:
    print("صعودی")
elif numbers == n_num:
    print("نزولی")
else:
    print("نامرتب")

