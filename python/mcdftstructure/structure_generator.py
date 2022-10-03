from collections import defaultdict
import random
from copy import deepcopy
from itertools import combinations


def swap_atoms(old_atoms):
    atoms = deepcopy(old_atoms)
    index = defaultdict(list)
    for atom in atoms:
        index[atom.symbol].append(atom.index)
    elements = list(index.keys())
    swap_elements = random.choice(list(combinations(elements, 2)))
    idx1 = random.choice(index[swap_elements[0]])
    idx2 = random.choice(index[swap_elements[1]])
    atoms[idx1].symbol = swap_elements[1]
    atoms[idx2].symbol = swap_elements[0]
    return atoms
