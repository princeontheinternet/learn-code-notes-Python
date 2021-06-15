
with open("sample.txt", 'a') as sample_file:
    for i in range(10):
        for j in range(10):
            print(f"{i + 1} times {j + 1} is {(i + 1) * (j + 1)}", file=sample_file)
        print("*" * 80, file=sample_file)