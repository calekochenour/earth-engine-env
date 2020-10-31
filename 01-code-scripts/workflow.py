"""
-------------------------------------------------------------------------------
 Module to set up the Earth Engine Python API for use in Jupyter environments
 and Google Colab.

 This module contains functions that differ in style from some PEP 8 and other
 Python conventions in order to centralize, consolidate, and modularize the
 setup process to fit both Jupyter envrionments (Jupyter Notebook, JupyterLab,
 Binder) and the Google Colab environment.
-------------------------------------------------------------------------------
"""


def initialize_earth_engine():
    """Initializes the Earth Engine Python API.

    Returns
    -------
    str

    Example
    -------
        >>> initialize_earth_engine()
        Imported ee. Initialized Earth Engine Python API.
    """
    # Import ee if not already imported
    import sys
    if "ee" not in sys.modules:
        import ee
        global ee

    # Initialize Earth Engine Python API
    try:
        ee.Initialize()
    except Exception:
        ee.Authenticate()
        ee.Initialize()

    return print("Imported ee. Initialized Earth Engine Python API.")


def import_geemap():
    """Imports the geemap package (environment-dependent, Google Colab
    vs. Jupyter/Binder).

    Returns
    -------
    environment : str
        Message indicating the geemap has been imported into the
        environment. The message differs based on the environment.

    Example
    -------
        >>> import_geemap()
        Notebook running in Jupyter/Binder. Imported geemap as gm.
    """
    # Check for Google Colab
    try:
        import google.colab
    # Notebook running in Jupyter/Binder
    except ImportError:
        running_in_colab = False
    # Notebook running in Google Colab
    else:
        running_in_colab = True

    # Import geemap based on environment (Google Colab vs. Jupyter/Binder)
    if running_in_colab:
        import subprocess
        subprocess.check_call(["python", "-m", "pip", "install", "geemap"])
        import geemap.eefolium as gm
        global gm
        environment = print(
            "Notebook running in Google Colab. Imported geemap.folium as gm."
        )
    else:
        import geemap as gm
        global gm
        environment = print(
            "Notebook running in Jupyter/Binder. Imported geemap as gm."
        )

    return environment
