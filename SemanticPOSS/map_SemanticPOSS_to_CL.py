import argparse, os
import numpy as np
from SemanticPOSS.map_SemanticPOSS_to_CL import SEMANTICPOSS_TO_CL

labels = 'labels/'
pc = 'velodyne/'
extension = '.bin'

def read_and_apply_CL(root,seq,frame):
    frame_name = str(int(frame)).zfill(6) + extension
    seq_name = os.path.join(root, str(int(seq)).zfill(2))

    path_pc = os.path.join(seq_name, os.path.join(pc, frame_name))
    path_labels = os.path.join(seq_name, os.path.join(labels, frame_name))

    pointcloud = np.fromfile(path_pc, dtype=np.float32, count=-1).reshape([-1,4])
    labels_read = np.fromfile(path_labels, dtype=np.uint32)
    sem_label = labels_read & 0xFFFF  
    coarse_sem_label = np.zeros(sem_label.shape)

    for k in range(len(sem_label)):
        coarse_sem_label[k] = SEMANTICPOSS_TO_CL[sem_label[k]]

    coarse_sem_label = coarse_sem_label.astype(np.int)

    return coarse_sem_label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to check", default="00")
    parser.add_argument("--frame", "-f", help="frame number we want to check", default="000000")
    parser.add_argument("--directory", "-d", help="location of the semanticPOSS folder")
    parser.add_argument("--saved", help="flag to save or not the relabelized frame", default=False)
    args = parser.parse_args()

    root_path = os.path.join(args.directory,'SemanticPOSS/dataset/sequences/')
    coarse_sem_label = read_and_apply_CL(root_path, args.sequence, args.frame)

    if args.saved:
        np.save('semanticPOSS_{}_{}_to_macro.bin'.format(args.sequence,args.frame), coarse_sem_label)
    