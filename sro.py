from itertools import combinations_with_replacement
import numpy as np
from ase.io import read, write
from ase.visualize import view
from ase.neighborlist import neighbor_list
from collections import Counter
from collections import defaultdict
from pathlib import Path


class SRO:
    def __init__(self, atoms, cutoffs) -> None:
        cutoffs.sort(reverse=True)
        self.atoms = atoms
        self.cutoffs = cutoffs
        self.elements = list(self.atoms.symbols)
        self.atom_dict = {k: v for k, v in enumerate(self.elements)}
        self.atom_ratio = {
            key: Counter(self.elements)[key] / sum(Counter(self.elements).values())
            for key in Counter(self.elements).keys()
        }
        self._total_bond = []
        self.ndatas = self.get_neighbor_count()

    def get_neighbor_count(self):
        nth_shell_counts = []
        for cutoff in self.cutoffs:
            i, j = neighbor_list("ij", self.atoms, cutoff)
            self._total_bond.append(len(i))
            data = defaultdict(list)
            for p, q in zip(i, j):
                data[self.atom_dict[p]].append(self.atom_dict[q])
            nth_shell_counts.append({key: Counter(data[key]) for key in data.keys()})

        # print(len(nth_shell_counts))

        for idx in range(len(nth_shell_counts) - 1):
            for key in nth_shell_counts[idx].keys():
                nth_shell_counts[idx][key].subtract(nth_shell_counts[idx + 1][key])
        return nth_shell_counts

    def get_sro(self, A, B):
        sros = []
        for shell_number in range(len(self.cutoffs)):

            R_AB_random = self.atom_ratio[A] * self.atom_ratio[B] * self._total_bond[shell_number]
            R_AB_mc = self.ndatas[shell_number][A][B]
            sros.append((1 - R_AB_mc / R_AB_random))
        return sros

    def write_sro(self, filename):
        sro_data = {}
        elements_pair = combinations_with_replacement(self.elements, 2)

        for A, B in elements_pair:
            sro1 = self.get_sro(A, B)
            sro_data[f"{A}{B}"] = sro1
            # sro2 = self.get_sro(B, A)
            # sro_data[f"{B}{A}"] = sro2

        with open(filename, "w") as f:

            for key, value in sro_data.items():
                value = list(np.around(np.array(value), 4))
                f.write(f"{key}:{',  '.join(map(str,value))}\n")


if __name__ == "__main__":
    # HEA1,2 is
    file = Path(__file__).parent / "./test_data/CONTCAR-HEA1-T100"
    atoms = read(file)
    cutoffs = [
        2.872,
        3.00,
    ]
    sro = SRO(atoms, cutoffs)
    sro.write_sro("HEA1-T100_sro.txt")
