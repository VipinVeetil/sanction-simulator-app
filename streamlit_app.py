"""Streamlit Community Cloud entry point for the Sanction Simulator.

The whole app (model, GUI, and OECD ICIO 2022 benchmark data) ships in
the PyPI package `sanction-simulator` (see requirements.txt); this shim
just runs the packaged GUI script. Bump the pinned version in
requirements.txt to deploy a new release.
"""

import os
import runpy

import sanction_simulator as ss

runpy.run_path(os.path.join(ss._PKG_DIR, "sanction_gui.py"),
               run_name="__main__")
