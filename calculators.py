from ase.calculators.vasp import Vasp
from abc import ABC, abstractclassmethod


class calculator(ABC):
    @abstractclassmethod
    def calculate_energy(self):
        pass

    @abstractclassmethod
    def calculate_dE(self):
        pass


class vasp_calculator(calculator):
    def __init__(self, atoms, dir, command):
        self.atoms = atoms
        self.dir = dir
        self.command = command

    @property
    def structure(self):
        return self.atoms

    @structure.setter
    def structure(self, atoms):
        self.atoms = atoms

    def calculate_energy(self, mc_step):
        calc_dir = self.dir + f"/{mc_step}"
        calc = Vasp(
            directory=calc_dir,
            command=self.command,
            ibrion=-1,
            isif=2,
            ialgo=48,
            nsw=0,
            ismear=0,
            sigma=0.1,
            ediff=0.1e-04,
            prec="Normal",
            xc="PBE",
            lreal="Auto",
            ncore=8,
        )
        self.atoms.pbc = True
        self.atoms.calc = calc
        self.atoms.get_potential_energy()
        return self.atoms.get_potential_energy()

    def calculate_dE(self, Ei, Ef):
        dE = Ef - Ei
        return dE
