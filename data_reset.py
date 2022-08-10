import csv

for i in range(1, 39):
    filename = "data_learn/line{}.csv".format(i)
    f = open(filename, "w")
    writer = csv.writer(f)
    data = [[0,-1]]
    writer.writerows(data)
    f.close()
