InFE
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Individualized FE repo.

The aim of this project is to create a open source workflow to create
Statistical Shape Models (SSMT). By segmenting volume from human test
samples and morphing a FE model to the segmented volume through
Landmarks. Different morphed volumes are then aligned in space with
General Procrustes Analysis (GPA). Pricipal Component Analysis (PCA) is
performed on the morphed mesh to extract the principal components. From
this point,the component extracted from PCA and features from the
specific subject (such as age, sex .. ) will be mapped through a
regression model to create a statistical shape model.

So the project is divided in different speps such: S

- Segmentation and Landmarking from 3D slicer
- Morphing with pygem
- General Procrustes Analysis (GPA) with scipy
- Principal Component Analysis (PCA) with scikit-learn
- Regression with scikit-learn –\> Subject FE

## Install

``` sh
pip install InFE
```

## How to use

Fill me in please! Don’t forget code examples:

``` python
1+1
```

    2
