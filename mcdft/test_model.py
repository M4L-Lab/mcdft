from dd_mcdft.file_io import FileIO
from dd_mcdft.prediction_algorithm import predict_energy
from sklearn.metrics import r2_score
import numpy as np
import time


class ML_tester:
    def __init__(self, trainer, out_filename):
        self.trainer = trainer
        self.out_file = FileIO(out_filename)

    def test(self):
        for i in range(self.trainer.train_size, len(self.trainer.all_clusters)):
            t1 = time.time()
            new_cluster = self.trainer.all_clusters[i]
            pred_E = predict_energy(
                self.trainer, new_cluster
            )
            real_E = self.trainer.all_energy[i]

            if pred_E is None:
                self.trainer.refit(new_cluster, real_E)
                delta_time = self.trainer.all_time[i]
                msg = f"{i:5} {real_E:10.5f} {str(np.nan):>11} {str(np.nan):>11} 1 {delta_time:20.3f}"
            else:
                delta_time = time.time() - t1
                err = pred_E - real_E
                
            
            self.out_file.write_formatted_message(msg)
            if(i%10==0):
                print('-', end='')