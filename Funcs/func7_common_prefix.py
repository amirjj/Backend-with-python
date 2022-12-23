a = ["hell", "hello world", "hello"]

s = list(zip(*a))
print(s)
tmp = ""
for el in s:
    if len(set(el)) != 1:
        break
    tmp += el[0]
# r = list(zip(*s))
# print(r)

print(tmp)