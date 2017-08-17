import numpy as np

data = np.genfromtxt("data/planets.csv", delimiter=',',skip_header=1, dtype=None)
print(data[1]) 

