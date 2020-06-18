import csv
import pandas as pd
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r')
rdr = csv.reader(f)

arr = []
arr2 = []
for line in rdr:
    if line == 0:
        print("pass")
    else:
        arr.append(line[3])
        arr2.append(line[4])

temp = pd.DataFrame(
    {"temp": arr, "hum": arr2}
)

plt.scatter(temp['temp'], temp['hum'], marker="o")
plt.xlabel('기온')
plt.ylabel('습도')
plt.show()
