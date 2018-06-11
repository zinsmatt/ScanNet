# ScanNet Benchmark Scripts

We provide scripts for evaluation of the tasks in the [ScanNet benchmark](TODO LINK), as well as some helper scripts which prepare and visualize data.

## Evaluation Scripts
The evaluation for both 2D and 3D semantic label and instance segmentation tasks are adapted from the [CityScapes evaluation](https://github.com/mcordts/cityscapesScripts), and provided in [2d_evaluation](2d_evaluation) and [3d_evaluation](3d_evaluation), respectively.

Note that visualization and data preparation scripts depend on the ScanNet label mapping file `scannetv2-labels.combined.tsv` to convert labels into the NYUv2 40-label set, which we use for evaluation.

Please see the [benchmark evaluation documentation](http://kaldir.vc.in.tum.de/scannet_benchmark/documentation) for more information about evaluation data formats and label sets.

## Helper Scripts
* 2D:
  * [2d_helpers](2d_helpers) contains helper scripts for converting ScanNet label images (`*_2d-label.zip`, `*_2d-label-filt.zip`) to the NYUv2 40-label set as 8-bit `png`s, as well as converting ScanNet instance images (`*_2d-instance.zip`, `*_2d-instance-filt.zip`) to 16-bit `png`s containing `[NYUv2 40-label]*1000+instance_id`. An already pre-processed subset of approximately 25,000 frames is available to download with the ScanNet download. 
  * `util.visualize_label_image` and `util.visualize_instace_image` can be used to visualize these processed label and instance images (assumes NYUv2 40 labels).

* 3D:
  * [3d_helpers](3d_helpers) contains helper scripts for exporting a train scan into the 3D evaluation format for semantic instance and label segmentation.
  * `3d_helpers/visualize_labels_on_mesh` can be used to visualize semantic labels on a mesh (assumes NYUv2 40 labels).
