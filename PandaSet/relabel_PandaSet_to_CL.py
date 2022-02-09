import argparse, os
import numpy as np
from PandaSet.map_PandaSet_to_CL import read_and_apply_CL

pc = 'lidar/'
annotations = 'annotations/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to check", default="00")
    args = parser.parse_args()

    root_path = os.path.join(args.directory,'SemanticKITTI/dataset/sequences/')
    seq_name = os.path.join(root_path, str(int(args.sequence)).zfill(3))
    annotation_name = os.path.join(seq_name, annotations)

    os.makedirs(os.path.join(annotation_name,'coarse_labels'), exists_ok=True)

    for frame in os.listdir(os.path.join(seq_name,pc)):
        frame_number = int(frame[:-7])
        coarse_sem_label = read_and_apply_CL(root_path, args.sequence, frame_number)
        np.save(os.path.join(os.path.join(annotation_name,'coarse_labels'), frame_number + '.bin'), coarse_sem_label)