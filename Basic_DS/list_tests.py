l = [1, 2, 3, 4, 5]
#retrieval
l.pop()
l.pop(2)

#appending
l.append("john")

#list slicing
l[2:5]
l[2:]
l[-3: -1]
l[1:5]
l[1:5:2]
l[::2]
l[::1]
l[::-1]

#list reference
l2 = l
l2.append(2)
print(l)
l3 = l.copy()
l3.append(4)
dir(l)

l.extend(l3)
l.remove(2)
l.reverse()
new_list = reversed(l)
# l.sort()
# sorted(l)

l4 = list()
