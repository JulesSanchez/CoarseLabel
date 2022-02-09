import argparse, os
import numpy as np
import pandas as pd
from PandaSet.map_PandaSet_to_CL import PANDASET_TO_CL

labels = 'annotations/semseg/'
pc = 'lidar/'
extension ='.pkl.gz'

def read_and_apply_CL(root,seq,frame):
    frame_name = str(int(frame)).zfill(2) + extension
    seq_name = os.path.join(root, str(int(seq)).zfill(3))

    path_pc = os.path.join(seq_name, os.path.join(pc, frame_name))
    path_labels = os.path.join(seq_name, os.path.join(labels, frame_name))

    pointcloud = pd.read_pickle(path_pc).to_numpy()[:,:4]
    sem_label = pd.read_pickle(path_labels).to_numpy()[:,0]
    coarse_sem_label = np.zeros(sem_label.shape)

    for k in range(len(sem_label)):
        coarse_sem_label[k] = PANDASET_TO_CL[sem_label[k]]

    coarse_sem_label = coarse_sem_label.astype(np.int)

    return coarse_sem_label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to check", default="001")
    parser.add_argument("--frame", "-f", help="frame number we want to check", default="00")
    parser.add_argument("--directory", "-d", help="location of the pandaset folder")
    parser.add_argument("--saved", help="flag to save or not the relabelized frame", default=False)
    args = parser.parse_args()

    root_path = os.path.join(args.directory,'Pandaset/')
    coarse_sem_label = read_and_apply_CL(root_path, args.sequence, args.frame)

    if args.saved:
        np.save('pandaset_{}_{}_to_macro.bin'.format(args.sequence,args.frame), coarse_sem_label)
    