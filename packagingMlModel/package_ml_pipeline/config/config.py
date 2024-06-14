import pathlib
import package_ml_pipeline
import os

ROOT_DIR=pathlib.Path(package_ml_pipeline.__file__).resolve().parent

print(ROOT_DIR)