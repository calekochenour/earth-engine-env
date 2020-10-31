# Earth Engine Conda Environment

This repository contains a Conda environment to work with the Google Earth Engine Python API via Jupyter environments and Python scripts.

## Prerequisites

To run the code in the `01-code-scripts/` folder locally or online with Binder or Google Colab, you will need:

 * [Google Earth Engine](https://earthengine.google.com/) account

If running code locally, you will also need:

 * Conda ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/))

## Binder Setup Instructions

Click the icon below to launch the project with Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/calekochenour/earth-engine-environment/main)

## Google Colab Setup Instructions

Click the icon below to launch the project with Google Colab:

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/calekochenour/earth-engine-environment/blob/master/01-code-scripts)

## Local Setup Instructions

Local instructions expect the user has cloned or forked the GitHub repository.

In a terminal, navigate to the folder containing the local repository.

### Create and Activate Conda Environment

From the terminal, you can create and activate the Conda environment.

Create environment:

```bash
conda env create -f environment.yml
```

Activate environment:

```bash
conda activate earth-engine-python
```

## Contents

### `01-code-scripts/`

Contains all Python and Jupyter Notebook files to use the Conda environment and the Earth Engine Python API Functionality.

### `environment.yml`

Contains all information to create the Conda environment required to run the Python and Jupyter Notebook files in the `01-code-scripts/` folder.  
