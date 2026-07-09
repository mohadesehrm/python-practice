sen1 = input("انشا را وارد کنید: ")
sen = sen1.split()
print("Words:", len(sen))
longest = sen[0]
for word in sen:
    if len(word) > len(longest):
        longest = word
print("Longest:", longest)
most = ""
max_count = 0
for ch in sen1:
    if ch != " ":
        if sen1.count(ch) > max_count:
            max_count = sen1.count(ch)
            most = ch
print("Most repeated char:", most)