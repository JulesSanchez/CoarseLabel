import argparse, os
import numpy as np
import open3d as o3d
from KITTI360.map_KITTI360_to_CL import read_and_apply_CL

labels = 'labels/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to process", default="00")
    args = parser.parse_args()

    root_path = os.path.join(args.directory,'KITTI-360/data_3d_labels/')
    seq_name = os.path.join(root_path, '2013_05_28_drive_'+str(int(args.sequence)).zfill(4)+'_sync')

    os.makedirs(os.path.join(seq_name,'coarse_labels'), exists_ok=True)

    for frame in os.listdir(os.path.join(seq_name,labels)):
        frame_number = int(frame[:-4])
        coarse_sem_label = read_and_apply_CL(args.directory, args.sequence, frame_number)
        np.save(os.path.join(os.path.join(seq_name,'coarse_labels'), frame), coarse_sem_label)