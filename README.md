# CoarseLabel
Helper functions and illustrations of **COLA: COarse LAbel pre-training for 3D semantic segmentation of sparse LiDAR datasets**.

![Coarse Labels](figures/CoarseLabels.png "Coarse Labels")


Each dataset folder present the following configuration:

- DatasetName
    - map_DatasetName_to_CL.py (can be launched to read (and optionnaly save) a frame for the target dataset with the coarse labels)
    - table_DatasetName_to_CL.py (map the original label of the target dataset to the coarse labels)
    - relabel_DatasetName_to_CL.py (relabel a full sequence of a dataset)

An example to save Coarse Labels from the frame 10 of the sequence 03 SemanticKITTI:

`python SemanticKITTI/map_SemanticKITTI_to_CL.py -f 10 -s 3 -d semanticKITTIDirectory --saved 1`

An other example to process the full sequence 03 of SemanticKITTI:

`python SemanticKITTI/relabel_SemanticKITTI_to_CL.py -s 3 -d semanticKITTIDirectory`


If you use the coarse labels please cite us.




