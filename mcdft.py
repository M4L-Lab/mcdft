from ase import Atoms, Atom
from ase.io import read, write
from itertools import combinations
from structure_generator import swap_atoms
from calculators import vasp_calculator
import random
import math
import numpy as np
from ase.io.trajectory import Trajectory
from ase.calculators.vasp import Vasp
import os


class MCDFT:
    def __init__(self, atoms, calculator, e, Temp, N, traj):
        self.atoms = atoms
        self.calculator = calculator
        self.structures = [atoms]
        self.energy = [e]
        self.Temp = Temp
        self.N = N
        self.traj = traj

    def monte_carlo(self, dE):
        kB = 1.0 / 11604.0
        prob = min(math.exp(-dE / (kB * self.Temp)), 1.0)
        accept = 1
        if prob < random.random():
            accept = 0
        return accept

    def build_traj(self):

        for i in range(1, self.N):
            atoms = swap_atoms(self.structures[-1].copy())
            self.calculator.structure = atoms
            e = self.calculator.calculate_energy(i)
            dE = self.calculator.calculate_dE(self.energy[-1], e)
            accept = self.monte_carlo(dE)
            atoms.info["accept"] = accept
            if self.traj is not None:
                self.traj.write(atoms)
            if accept:
                self.structures.append(atoms)
                self.energy.append(e)
