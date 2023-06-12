#!/bin/sh
pip install pandas
pip install numpy
pip install scikit-learn
python data_creation.py
python model_preprocessing.py
python model_preparation.py
python model_testing.py