import numpy as np
from sklearn.neighbors import LocalOutlierFactor
from sklearn.linear_model import Ridge, Lasso


class ML_trainer:
    """Read csv file, make dataset from based on train_size
    and save the model"""

    def __init__(self, train_size, csv_file, n_neighbors=5):
        self.csv_file = csv_file
        self.train_size = train_size
        self.n_neighbors = n_neighbors
        self.lof_model = LocalOutlierFactor(n_neighbors=n_neighbors, novelty=True)
        self.ml_model = Ridge(alpha=0.001)
        self.training_atoms_idx = []
        self._get_data_from_csv()
        self.get_training_data()

    def _get_data_from_csv(self):
        data = np.loadtxt(self.csv_file, delimiter=",")
        self.all_clusters = data[:, :-2]
        self.all_energy = data[:, -2]
        self.all_time = data[:, -1]
        self.training_clusters = data[: self.train_size, :-2]
        self.training_energy = data[: self.train_size, -2]

    def get_training_data(self):
        dX_train = []
        dY_train = []
        for i in range(self.train_size - 1):
            for j in range(i):
                dX_train.append(self.training_clusters[j] - self.training_clusters[i])
                dY_train.append(self.training_energy[j] - self.training_energy[i])
        self.dX_train = np.array(dX_train)
        self.dY_train = np.array(dY_train)

    def train_model(self):
        print(self.dX_train.shape)

        self.lof_model.fit(self.dX_train)
        self.ml_model.fit(self.dX_train, self.dY_train)

    def refit(self, new_cluster, new_energy):
        new_cluster = new_cluster.reshape(1, -1)
        new_energy = np.array([new_energy])
        new_dX = new_cluster - self.training_clusters
        new_dY = new_energy - self.training_energy
        self.ml_model.fit(new_dX, new_dY)
        self.training_clusters = np.append(self.training_clusters, new_cluster, axis=0)
        self.training_energy = np.append(self.training_energy, new_energy, axis=0)

        self.lof_model.fit(new_dX)
