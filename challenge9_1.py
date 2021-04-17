my_list = []

with open("csvreading.py", "rt") as f:
    for line in f:
        my_list.append(line)

print(my_list)
