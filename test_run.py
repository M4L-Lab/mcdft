from calculators import vasp_calculator
from ase.io import read
from ase.io.trajectory import Trajectory
from mcdft import MCDFT
import numpy as np
import os


N = 50
Temp = 100
cmd = "mpirun -n 64 ~/data/Software/vasp_std"
atoms = read("POSCAR_AsP_seg")
dir = os.getcwd()
traj = Trajectory(dir + "/test_mcdft_AsP_seg.traj", "w")
calc = vasp_calculator(atoms, dir, cmd)
e = calc.calculate_energy(mc_step=0)
mcdft = MCDFT(atoms, calc, e, Temp, N, traj)
