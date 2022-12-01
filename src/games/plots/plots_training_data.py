#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:17:53 2022

@author: kate
"""
from typing import List, Tuple
import matplotlib.pyplot as plt


def plot_training_data_2d(
    x_values: List[float],
    y_sim: List[float],
    y_exp: List[float],
    y_exp_error: List[float],
    filename: str,
    plot_settings: Tuple[str, str, str, str, str],
    context: str,
) -> None:
    """Plots a 2-dimensional figure.

    Parameters
    ----------
    x_values
        list of floats defining the independent variable

    y_sim
        list of floats defining the simulated dependent variable

    y_exp
        list of floats defining the experimental dependent variable

    y_exp_error
        list of floats defining the experimental error for the dependent variable

    filename
       string defining the filename used to save the plot

    plot_settings
        a list of strings defining the plot settings

    context
        a string defining the absolute path to src/games

    Returns
    -------
    None
    """
    plt.style.use(context + "paper.mplstyle.py")
    x_label, y_label, x_scale, plot_color, marker_type = plot_settings
    plt.figure(figsize=(3, 3))
    plt.plot(x_values, y_sim, linestyle="dotted", marker="None", label="sim", color='rebeccapurple')
    plt.errorbar(
        x_values,
        y_exp,
        marker=marker_type,
        yerr=y_exp_error,
        color=plot_color,
        ecolor=plot_color,
        markersize=6,
        fillstyle="none",
        linestyle="none",
        capsize=2,
        label="exp",
    )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xscale(x_scale)
    plt.legend()
    plt.savefig("./" + filename + ".svg", dpi=600)
