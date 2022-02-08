# CoarseLabel
Helper functions and illustrations of **COLA: COarse LAbel pre-training for 3D semantic segmentation of sparse LiDAR datasets**.

![Coarse Labels](figures/CoarseLabels.png "Coarse Labels")


Each dataset folder present the following configuration:

- DatasetName
    - read_DatasetName_frame.py (can be launched to read (and optionnaly save) a frame for the target dataset with the coarse labels)
    - config_DatasetName.yaml (contain the information needed regarding folder path to read frames)
    - map_DatasetName_to_CL.json (map the original label of the target dataset to the coarse labels)

If you use the coarse labels please cite us.




