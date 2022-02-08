# CoarseLabel
Helper functions and illustrations of **COLA: COarse LAbel pre-training for 3D semantic segmentation of sparse LiDAR datasets**.

![Coarse Labels](figures/CoarseLabels.png "Coarse Labels")


Each dataset folder present the following configuration:

- DatasetName
    - read_DatasetName_frame.py (can be launched to read (and optionnaly save) a frame for the target dataset with the coarse labels)
    - map_DatasetName_to_CL.py (map the original label of the target dataset to the coarse labels)

An example to save Coarse Labels from the frame 10 of the sequence 03 SemanticKITTI:

`python SemanticKITTI/read_SemanticKITTI_frame.py -f 10 -s 3 -d folderDirectory -s 1`

If you use the coarse labels please cite us.




