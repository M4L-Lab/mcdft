from ase import Atoms, Atom
from ase.io import read, write
from itertools import combinations
from dd_mcdft.structure_generator import swap_atoms
from dd_mcdft.prediction_algorithm import predict_energy_mc
import random
import math
import numpy as np
from ase.io.trajectory import Trajectory

import os


class MCDFT:
    def __init__(
        self,
        atoms,
        trainer,
        cluster_calculator,
        e,
        Temp,
        traj,
        file_io,
        MAX_MCSTEPS=5000,
    ):
        self.atoms = atoms
        self.trainer = trainer
        self.cluster_calculator = cluster_calculator
        self.structures = [atoms]
        self.energy = [e]
        self.Temp = Temp
        self.traj = traj
        self.MAX_MCSTEPS = MAX_MCSTEPS
        self.file_io = file_io
        self.N_dft = 0
        self.MC_step = 0
        self.last_dft_at = []

    def monte_carlo(self, dE):
        kB = 1.0 / 11604.0
        prob = min(math.exp(-dE / (kB * self.Temp)), 1.0)
        accept = 1
        if prob < random.random():
            accept = 0
        return accept

    def build_traj(self):
        while self.MC_step < self.MAX_MCSTEPS:
            atoms = swap_atoms(self.structures[-1].copy())
            atoms_data = self.cluster_calculator.extract_feature([atoms])[0]
            new_cluster = atoms_data.reshape(1, -1)

            e, p_neg= predict_energy_mc(self.trainer, new_cluster)
            if e is not None:
                dE = e - self.energy[-1]
                accept = self.monte_carlo(dE)
                atoms.info["accept"] = accept
                atoms.info["E_calc"] = e

                msg = f"{self.MC_step} {p_neg} {e:10.5f} {(e-self.energy[0]):10.5f}"
                self.file_io.write_formatted_message(msg)

                print(msg)
                if self.traj is not None:
                    self.traj.write(atoms)
                if accept:
                    self.structures.append(atoms)
                    self.energy.append(e)

            self.MC_step += 1
