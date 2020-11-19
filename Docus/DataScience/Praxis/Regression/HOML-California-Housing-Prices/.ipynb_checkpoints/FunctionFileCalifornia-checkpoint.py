# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals



# Common imports
import numpy as np
import os
import pandas as pd

# to make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Basic Variables
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "end_to_end_project"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
print(IMAGES_PATH)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    os.makedirs(IMAGES_PATH, exist_ok=True) # Erstelle den Folder wenn er nicht existiert
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Ignore useless warnings (see SciPy issue #5998)
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")



def load_housing_data(housing_path=HOUSING_PATH, filename="housing.csv"):
    csv_path = os.path.join(housing_path, filename)
    return pd.read_csv(csv_path)


def plot_pred_act(prediction, actual):
    
    r_min = actual.min()
    r_max = actual.max()
    
    red_color = '#d5042a'
    orange_color = '#ED7D31'
    blue_color = '#43bed8'
    lightgreen_color = '#98c235'
    darkgreen_color = '#0b8f6a'
    darkblue_color = '#0062A7'
    lightblue_color = '#4DBED3'    
    
    plt.figure(figsize=(8,8))
    plt.scatter(
        y=prediction,
        x=actual,
        alpha=0.2,
        marker=".",
        color=lightgreen_color
    )
    plt.xlim(r_min, r_max)
    plt.ylim(r_min, r_max)
    plt.plot([r_min, r_max], [r_min, r_max], "-", color=red_color)
    plt.title("Prediction vs Actual")
    plt.xlabel("actual")
    plt.ylabel("predicted")