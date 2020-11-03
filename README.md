[![Travis CI Build Status](https://travis-ci.com/calekochenour/earth-engine-environment.svg?branch=main)](https://travis-ci.com/calekochenour/earth-engine-environment)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/32r7s2skrgm9ubva?svg=true)](https://ci.appveyor.com/project/calekochenour/earth-engine-environment)


[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/calekochenour/earth-engine-environment/main)
[![Launch Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/calekochenour/earth-engine-environment/blob/main/01-code-scripts/01-qualitative-change-detection.ipynb)
[![BSD 3-Clause License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Earth Engine Conda Environment

This repository contains a Conda environment to use the Google Earth Engine Python API within Jupyter environments and Python scripts.

## Prerequisites

To run the code in the `01-code-scripts/` folder locally or online with Binder or Google Colab, you will need:

 * [Google Earth Engine](https://earthengine.google.com/) account

If running code locally, you will also need:

 * Conda ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/))

## Binder Setup Instructions

Click the icon below to launch the project with Binder:

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/calekochenour/earth-engine-environment/main)

## Google Colab Setup Instructions

Click the icon below to launch the project with Google Colab:

[![Launch Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/calekochenour/earth-engine-environment/blob/main/01-code-scripts/01-qualitative-change-detection.ipynb)

## Local Setup Instructions

Local instructions expect the user has cloned or forked the GitHub repository. In a terminal, navigate to the folder containing the local repository.

From the terminal, you can create and activate the Conda environment.

Create environment:

```bash
$ conda env create -f environment.yml
```

Activate environment:

```bash
$ conda activate earth-engine-python
```

## Contents

### `01-code-scripts/`

Contains all Python and Jupyter Notebook files to demonstrate the functionality of the Conda environment and the Earth Engine Python API.

### `environment.yml`

Contains information to create the Conda environment required to run the Python and Jupyter Notebook files in the `01-code-scripts/` folder.  
