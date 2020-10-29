import matplotlib.pyplot as plt

dataset_x = []
files = open("dataset_x.txt","r")
for file in files:
    dataset_x.append(float(file))

dataset_y = []
files = open("dataset_y.txt", "r")
for file in files:
    dataset_y.append(float(file))

plt.figure(figsize=(7,5))
plt.scatter(dataset_x,dataset_y, label='o', color='red', s=3)
plt.plot(dataset_x,dataset_y,color="blue",linewidth = 2)
plt.xlabel("index")
plt.ylabel("value of index")
plt.title("Visualization")
plt.savefig("visualization.png")
plt.show()
