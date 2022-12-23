names = {"john", "robert", "robert"}

sample_set = {1 ,2 ,3 , 4, 5}
sample_set.add(7)
sample_set.add(2)
#sets are not ordered, no guarantee the last one you add to be in the end of set 
sample_set.add(10)
sample_set.add(9)
#sets are not subscriptable
print(sample_set[1])

dir(sample_set)

another_set = {"a", "b", "1"}
sample_set.union(another_set)
print(sample_set)
sample_set.update(another_set)
print(sample_set)
sample_list = list(sample_set)

sample_set.difference(another_set)
sample_set - another_set
another_set.pop()
another_set.discard('b')
another_set.issubset(another_set)
