import numpy as np

data = np.genfromtxt("data/planets.csv", delimiter=',',skip_header=1, dtype=None)

m = data.shape[0]
n = data.shape[1]

som_dimensions = np.array([100, 100])
iterations = 100
learning_rate = 0.01

som = np.random.random((som_dimensions[0], som_dimensions[1], m))
init_radius = max(som_dimensions[0], som_dimensions[1])/2

print(data[1])
k = data[:, np.random.randint(0,n)].reshape(np.array([m, 1]))

def find_best(target, som, m):
    min_dist = np.iinfo(np.int).max
    idx = np.array([0, 0])
    for x in range(som.shape[0]):
        for y in range(som.shape[1]):
            w = som[x, y, :].reshape(m, 1)
            sq_dist = np.sum((w-target) **2)
            if sq_dist < min_dist:
                min_dist = sq_dist
                idx = np.array([x, y])
    best_match = some[idx[0], idx[1], :].reshape(m, 1)
    return best_match, idx

print(find_best(k, som, m))
def loop():
    # select random
    target = data[:, np.random.randint(0,n)].reshape(np.array([m,1]))
