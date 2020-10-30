import random
import matplotlib.pyplot as plt

dataset_x = []
output = "dataset_x.txt"
for i in range(0, 1000):
    num_100 = random.randint(1, 10000)
    dataset_x.append(num_100 / 100)
print(dataset_x)   
plt.hist(dataset_x, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
plt.show()

with open(output, 'w') as output_file:
    for i in dataset_x:
        output_file.writelines(str(i) + "\n")
    output_file.close()
