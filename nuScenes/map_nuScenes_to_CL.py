import argparse, os, json
import numpy as np
from nuScenes.table_nuScenes_to_CL import NUSCENES_TO_CL

labels = 'labels/'
pc = 'velodyne_points/data/'
extension = '.bin'

def read_and_apply_CL(root,seq,frame,scene_json):
    seq_name = 'scene-'+str(seq).zfill(4)
    frame_number = int(frame)

    path_pc = os.path.join(root_path, scene_json[seq_name]['file'][frame_number])
    path_labels = os.path.join(root_path, scene_json[seq_name]['label'][frame_number])

    pointcloud = np.fromfile(path_pc, dtype=np.float32).reshape((-1, 5))[:, :4]
    sem_label = np.fromfile(path_labels, dtype=np.uint8)
    coarse_sem_label = np.zeros(sem_label.shape)

    for k in range(len(sem_label)):
        coarse_sem_label[k] = NUSCENES_TO_CL[sem_label[k]]

    coarse_sem_label = coarse_sem_label.astype(np.int)

    return coarse_sem_label

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--sequence", "-s", help="sequence number we want to check", default="00")
    parser.add_argument("--frame", "-f", help="frame number we want to check", default="000000")
    parser.add_argument("--directory", "-d", help="location of the semanticPOSS folder")
    parser.add_argument("--saved", help="flag to save or not the relabelized frame", default=False)
    args = parser.parse_args()
    with open('nuScenes/semanticScenes.json') as json_file:
        scene_json = json.load(json_file)
    root_path = os.path.join(args.directory,'nuscenes')
    coarse_sem_label = read_and_apply_CL(root_path, args.sequence, args.frame, scene_json)

    if args.saved:
        np.save('nuscenes_{}_{}_to_macro.bin'.format(args.sequence,args.frame), coarse_sem_label)
    