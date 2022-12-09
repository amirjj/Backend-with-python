from time import time

first_ts = time()

# def regular_file_reader(filename):
#     file_ = open(filename, "r")
#     data = file_.readlines()
#     file_.close()
#     return data

# for row in regular_file_reader("sample_file.csv"):
#     continue
#     # print(row)
#     # global second_time
#     # second_time = time()
#     # break



def generator_file_reader(filename):
    with open(filename, "r") as f:
        for row in f:
            yield row


for row in generator_file_reader("sample_file.csv"):
    print(row)
    global second_time
    second_time = time()
    break
    continue

second_time = time()
print(second_time - first_ts)

"""
for reading first line of a file with 10M record, comparing reading with generator vs 
regular reading a file (reading the whole file first) improved significantly.
does this fact still correct if you want to read all file? No
"""


"""
While both return and yield statements are performing similarly on the time front, 
it is in the area of memory consumption where the generators really outshine the return statement.

https://www.pylenin.com/blogs/how-fast-are-generators/
"""