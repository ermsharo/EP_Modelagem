import pandas as pd
import ast
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame()
df = pd.read_csv("generic.csv")





winner_df_s = df[df["winner"] == "s"]


def calc_density(df):
    density=[]
    for row in df.itertuples():
        count = row.count_of_s
        area = row.s_points_area
        if((count/area) < 0.008):
            density.append((count/area))
    return density



density = calc_density(winner_df_s)
density.sort()

fig, ax = plt.subplots()
ax.hist(density, bins= 200,linewidth=1.5, edgecolor="blue")

plt.show()
