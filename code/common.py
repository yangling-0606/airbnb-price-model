"""Shared data loading, cleaning and plotting style for the Airbnb business case."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "Case 1 - Airbnb Dataset.csv"
FIG = ROOT / "outputs" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

# Colours: a coral and a teal, with warm greys (Airbnb-style)
CORAL, TEAL = "#ff385c", "#00a699"
INK, INK2, MUTED, GRID = "#222222", "#484848", "#8a8a8a", "#ebebeb"

# Friendly names used on every chart
LABELS = {
    "price": "Price",
    "log_price": "log(Price)",
    "person_capacity": "Guest capacity",
    "bedrooms": "Bedrooms",
    "is_entire_home": "Entire home/apt",
    "is_shared_room": "Shared room",
    "host_is_superhost": "Superhost",
    "multi": "Host flag: multi",
    "biz": "Host flag: biz",
    "cleanliness_rating": "Cleanliness rating",
    "guest_satisfaction_overall": "Guest satisfaction",
    "dist": "Distance to centre (km)",
    "metro_dist": "Distance to metro (km)",
    "attr_index_norm": "Attraction index (city-norm.)",
    "rest_index_norm": "Restaurant index (city-norm.)",
    "attr_index": "Attraction index (raw)",
    "rest_index": "Restaurant index (raw)",
    "weekday": "Weekday flag (1 = yes)",
}


def load() -> pd.DataFrame:
    """Load and enrich the dataset.

    Assumptions (documented for the interview):
    * VERIFIED IN THE DATA: `multi` and `biz` never co-occur (mutually exclusive flags);
      room_shared / room_private duplicate room_type.
    * `multi` and `biz` are used as given (0/1 flags); their meaning is not documented
      beyond the catalogue, so no interpretation is added.
    * `weekday` is used as given (0/1 flag); no interpretation is added.
    * `realSum` (called `price` from here on, for readability) is used in relative terms only; no stay length / guest count is assumed.
    * `room_shared` / `room_private` are one-hot duplicates of `room_type` -> dropped.
    """
    df = pd.read_csv(DATA)
    df = df.rename(columns={"realSum": "price"})          # shorter, clearer name (the catalogue calls it realSum)
    df["city"] = df["city"].str.title()
    df["is_entire_home"] = (df["room_type"] == "Entire home/apt").astype(int)
    df["is_shared_room"] = df["room_shared"].astype(int)
    df["host_is_superhost"] = df["host_is_superhost"].astype(int)
    df["log_price"] = np.log(df["price"])
    return df.drop(columns=["room_shared", "room_private"])


def style():
    plt.rcParams.update({
        "figure.dpi": 110, "savefig.dpi": 200, "savefig.bbox": "tight",
        "font.family": "sans-serif", "font.size": 13,
        "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK,
        "axes.titlesize": 15, "axes.titleweight": "bold", "axes.titlelocation": "left",
        "axes.labelsize": 13, "xtick.labelsize": 12, "ytick.labelsize": 12, "legend.fontsize": 12,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
        "xtick.color": INK2, "ytick.color": INK2,
        "xtick.major.size": 0, "ytick.major.size": 0,
        "legend.frameon": False,
    })


def save(fig, name):
    path = FIG / f"{name}.png"
    fig.savefig(path, facecolor="white")
    try:  # inside Jupyter: show the chart below the cell
        from IPython import get_ipython
        from IPython.display import display
        if get_ipython() is not None:
            display(fig)
    except ImportError:
        pass
    plt.close(fig)
    return path
