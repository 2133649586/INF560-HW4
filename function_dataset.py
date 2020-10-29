dataset_y = []
output = "dataset_y.txt"

files = open("create_dataset.txt","r")
for file in files:
    dataset_y.append(float(file)*3+6)

with open(output, 'w') as output_file:
    for i in dataset_y:
        output_file.writelines(str(i) + "\n")
    output_file.close()