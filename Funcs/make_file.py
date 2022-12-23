with open("sample_file.csv", "w") as f:
    for i in range(10000000):
        f.write(f"THis is row number {i}\n")

