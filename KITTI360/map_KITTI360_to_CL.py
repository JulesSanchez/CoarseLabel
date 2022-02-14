import argparse, os
import numpy as np
from KITTI360.table_KITTI360_to_CL import KITTI360_TO_CL


def read_and_apply_CL(root,seq,frame):
    frame_name = str(int(frame)).zfill(10) + extension
    seq_name_pc = os.path.join(os.path.join(root,'KITTI-360/data_3d_raw/'), '2013_05_28_drive_'+str(int(seq)).zfill(4)+'_sync')
    seq_name_label = os.path.join(os.path.join(root,'KITTI-360/data_3d_labels/'), '2013_05_28_drive_'+str(int(seq)).zfill(4)+'_sync')

    path_pc = os.path.join(seq_name_pc, os.path.join(pc, frame_name))
    path_labels = os.path.join(seq_name_label, os.path.join(labels, frame_name))

    pointcloud = np.fromfile(path_pc, dtype=np.float32, count=-1).reshape([-1,4])
    sem_label = np.fromfile(path_labels, dtype=np.int16)
    coarse_sem_label = np.zeros(sem_label.shape)

    for k in range(len(sem_label)):
        coarse_sem_label[k] = KITTI360_TO_CL[sem_label[k]]

    coarse_sem_label = coarse_sem_label.astype(np.int)

    return coarse_sem_label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to check", default="00")
    parser.add_argument("--frame", "-f", help="frame number we want to check", default="000000")
    parser.add_argument("--directory", "-d", help="location of the semanticPOSS folder")
    parser.add_argument("--saved", help="flag to save or not the relabelized frame", default=False)
    args = parser.parse_args()

    root_path = args.directory
    coarse_sem_label = read_and_apply_CL(root_path, args.sequence, args.frame)

    if args.saved:
        np.save('kitti360_{}_{}_to_macro.bin'.format(args.sequence,args.frame), coarse_sem_label)
    