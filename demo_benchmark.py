import numpy as np

seqs=np.array(['ADL-Rundle-1','ADL-Rundle-3','AVG-TownCentre','ETH-Crossing','ETH-Jelmoli','ETH-Linthescher','KITTI-16','KITTI-19','PETS09-S2L2','TUD-Crossing','Venice-1'])


for s in range(len(seqs)):
    single_tracker(seqs[s])
