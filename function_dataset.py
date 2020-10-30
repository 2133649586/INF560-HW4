
import random
import matplotlib.pyplot as plt

dataset_y = []
output = "dataset_y.txt"

files = open("dataset_x.txt","r")
for file in files:
    dataset_y.append(float(file)*3+6)

print(dataset_y)

plt.hist(dataset_y, bins=40, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
plt.show()

with open(output, 'w') as output_file:
    for i in dataset_y:
        output_file.writelines(str(i) + "\n")
    output_file.close()
