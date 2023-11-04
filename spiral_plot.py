import streamlit as st
import plotly.express as px
import pandas as pd
import random
import numpy as np


import plotly.io as pio
pio.templates.default = 'plotly'

# st.set_page_config(layout="wide")

random.seed(21412552)

data = {
    "year": [year for year in range(1950, 2021)],
}

size = len(data["year"])

data["rand"] = np.array([random.randrange(110, 140)/10 for _ in range(size)])
data["increase"] = np.array([np.exp(1 + x / 80) for x in range(size)])
data["temperature"] = data["rand"] + data["increase"]

df = pd.DataFrame(data)

df["theta"] = 360 * (df["year"] - df["year"].min()) / (df["year"].max() - df["year"].min())
df["year"] = df["year"].astype(str)

fig = px.bar_polar(
    df,
    r="temperature",
    theta="year",
    color="temperature",
    range_r=(11, df["temperature"].max() + 1),
    # labels="year",
    # title="Average Temperature per year (ºC)"
)

fig.update_layout(height=700)

# fig.write_image("spiral_plot.png")
st.title("Spiral plot per PAC 2 Visualitzacio de Dades")

st.header("Average Temperature (ºC) per year")

st.plotly_chart(fig, use_container_width=True)
