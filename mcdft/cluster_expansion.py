from icet import ClusterSpace
from icet.tools import map_structure_to_reference
import numpy as np


class cluster_expansion:
    def __init__(self, primitive_structure, cutoffs, chemical_symbols):
        self.primitive_structure = primitive_structure
        self.cutoffs = cutoffs
        self.chemical_symbols = chemical_symbols
        self.cs = ClusterSpace(
            structure=primitive_structure,
            cutoffs=cutoffs,
            chemical_symbols=chemical_symbols,
        )

    def extract_feature(self, all_atoms, map=True):
        cluster_vectors = []
        for atoms in all_atoms:
            ideal_structure, info = map_structure_to_reference(
                atoms, self.primitive_structure
            )
            cluster_vectors.append(self.cs.get_cluster_vector(ideal_structure))
        return np.array(cluster_vectors)

    def get_ideal_structure(self, atoms):
        ideal_structure, info = map_structure_to_reference(
            atoms, self.primitive_structure
        )

        return ideal_structure
