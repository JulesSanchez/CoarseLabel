import argparse, os
import numpy as np
import open3d as o3d
from KITTI360.map_KITTI360_to_CL import read_and_apply_CL

labels = 'labels/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to process", default="00")
    args = parser.parse_args()

    root_path = os.path.join(args.directory,'nuscenes')
    seq_name = 'scene-'+str(args.sequence).zfill(4)

    os.makedirs(os.path.join(root_path,'coarse_labels'), exists_ok=True)

    with open('nuScenes/semanticScenes.json') as json_file:
        scene_json = json.load(json_file)

    for frame_number in range(len(scene_json[seq_name]['label'])):
        frame_name = scene_json[seq_name]['label'][frame_number].split('/')[-1]
        coarse_sem_label = read_and_apply_CL(root_path, args.sequence, frame_number, scene_json)
        np.save(os.path.join(os.path.join(root_path,'coarse_labels'), frame_name), coarse_sem_label)