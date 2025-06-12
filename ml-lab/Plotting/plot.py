import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('iris.csv','r') as heartDisease_csv:
    plots = csv.reader(heartDisease_csv, delimiter=',')
    for row in plots:
        x.append(row[4])
        y.append(row[3])

plt.hist2d(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

