#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:36:16 2022

@author: kate
"""
from typing import Tuple, List
import pandas as pd
import numpy as np


def define_experimental_data(settings: dict) -> Tuple[List[float], List[float], List[float]]:
    """
    Imports experimental data

    Parameters
    ---------
    settings
       a dictionary of run settings

    Returns
    -------
    x
       a list of floats defining the independent variable for the given dataset

    exp_data_norm
       a list of floats defining the normalized dependent variable for the given
       dataset

    exp_error_norm
        a list of floats defining the normalized measurement error for
        the dependent variable for the given dataset
    """

    path = settings["context"] + "config/"
    filename = path + "training_data_" + settings["dataID"] + ".csv"
    df_exp = pd.read_csv(filename)
    x = list(df_exp["x"])
    exp_data = list(df_exp["y_raw"])
    exp_error = list(df_exp["y_err_raw"])

    if settings["dataID"] == "synTF dose response":
        if settings["normalizationID"] == 'max':
            exp_data_norm = [i / max(exp_data) for i in exp_data]
            exp_error_norm = [i / max(exp_data) for i in exp_error]
        elif settings["normalizationID"] == 'mean':
            exp_data_norm = [i / np.mean(exp_data) for i in exp_data]
            exp_error_norm = [i / np.mean(exp_data) for i in exp_error]
        elif settings["normalizationID"] == 'scaling factor':
            #use raw data - goal of scaling factor is to match simulated values to raw experimental data
            exp_data_norm = exp_data
            exp_error_norm = exp_error

    return x, exp_data_norm, exp_error_norm
