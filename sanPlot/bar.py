from matplotlib import pyplot as plt

plt.figure('seaborn')

dev_x = [1,2,3,4,5,6,7,8,9,10,11]
dev_y = [100,200,300,400,500,600,700,800,900,1000,11000]

plt.bar(dev_x, dev_y)

plt.xlabel("this is the x coordinate")
plt.ylabel("this is the y coordinate")

plt.title("line graph")
plt.show()