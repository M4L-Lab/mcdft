import numpy as np


def predict_energy_mc(trainer, new_cluster):
    new_dX_n = new_cluster - trainer.training_clusters

    p_neg = np.where(trainer.lof_model.predict(new_dX_n) == 1)

    if len(p_neg[0]) < 1:
        pred_E_n = np.average(
            trainer.training_energy + trainer.ml_model.predict(new_dX_n)
        )
        trainer.refit(new_cluster, pred_E_n)
        return pred_E_n, 0

    else:
        pred_E_n = np.average(
            trainer.training_energy[p_neg[0]]
            + trainer.ml_model.predict(new_dX_n)[p_neg[0]]
        )
        return pred_E_n, len(p_neg[0])
