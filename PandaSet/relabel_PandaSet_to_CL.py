import argparse, os
import numpy as np
import open3d as o3d
from SemanticKITTI.table_SemanticKITTI_to_CL import SEMANTICKITTI_TO_CL
from SemanticKITTI.map_SemanticKITTI_to_CL import read_and_apply_CL

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to check", default="00")
    args = parser.parse_args()

    root_path = os.path.join(args.directory,'SemanticKITTI/dataset/sequences/')
    seq_name = os.path.join(root, str(int(args.sequence)).zfill(2))

    os.makedirs(os.path.join(seq_name,'coarse_labels'), exists_ok=true)

    for frame in os.listdir(os.path.join(seq_name,pc)):
        frame_number = int(drame[:-4])
        coarse_sem_label = read_and_apply_CL(root_data, args.sequence, frame_number)
        np.save(os.path.join(os.path.join(seq_name,'coarse_labels'), frame), coarse_sem_label)