import numpy as np

def NaivePLA(perm=np.arange(400)):
    data = np.fromfile('./hw1_15_train.dat.txt', sep=' ').reshape((-1, 5))
    data = np.concatenate((np.ones((data.shape[0],1)), data), axis=1)
    X = data[perm, 0:5]
    Y = data[perm, 5]
    cycle_start = 0
    w = np.zeros((5,))
    step = 0
    n_updates = 0
    while step < 400: 
        idx = (cycle_start + step)%400
        if sign(w.dot(X[idx])) == Y[idx]:
            step += 1
        else:
            w += Y[idx]*X[idx]
            cycle_start = idx
            step = 1
            n_updates += 1
    return n_updates

def NaivePLARandPerm(n_sim=2000, eta=1):
    n_updates = np.zeros(n_sim)
    for i in range(n_sim):
        n_updates[i] = NaivePLA(np.random.permutation(400))
    return np.mean(n_updates)

def PocketPLA(n_updates=50, n_sim=2000):
    data_train =\
        np.fromfile('./hw1_18_train.dat.txt', sep=' ').reshape((-1, 5))
    data_train =\
        np.concatenate((np.ones((data_train.shape[0],1)), data_train),\
                       axis=1)
    X_train = data_train[:, 0:5]
    Y_train = data_train[:, 5]
    data_test =\
        np.fromfile('./hw1_18_test.dat.txt', sep=' ').reshape((-1, 5))
    data_test =\
        np.concatenate((np.ones((data_test.shape[0],1)), data_test),\
                       axis=1)
    error_rates = np.zeros(n_sim)
    w = np.zeros(5)
    w_pocket = np.zeros(5)
    for i in range(n_sim):
        j = 0
        while j < n_updates:
            idx = np.random.choice(X_train.shape[0])
            w = w + Y_train[idx]*X_train[idx]
            j += 1
            if ErrorRate(data_train, w) < ErrorRate(data_train, w_pocket):
                w_pocket = w
        error_rates[i] = ErrorRate(data_test, w_pocket)
    return np.mean(error_rates)


def ErrorRate(data, w):
    X = data[:, 0:5]
    Y = data[:, 5]
    prediction = [sign(w.dot(x)) for x in X]
    wrong = 0
    for i in range(Y.shape[0]):
        if prediction[i] != Y[i]:
            wrong += 1
    return wrong/Y.shape[0]


def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def main():
    x = 1



if __name__ == '__main__':
    main()
