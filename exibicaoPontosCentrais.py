import pandas as pd
import ast
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame()
df = pd.read_csv("generic.csv")


def string_to_list(str_of_list):
    res = ast.literal_eval(str_of_list)
    return res


winner_df_s = df[df["winner"] == "s"]
winner_df_r = df[df["winner"] == "r"]
winner_df_p = df[df["winner"] == "p"]


def validate_number_x(n):
    if n < 360 and n > 0:
        print("n->", n)
        return n
    return False

def validate_number_y(n):
    if n < 640 and n > 0:
        print("n->", n)
        return n
    return False


print("Create our simulation")
x_assis_s = []
y_assis_s = []
x_assis_r = []
y_assis_r = []
x_assis_p = []
y_assis_p = []


for row in winner_df_s.itertuples():
    s_center_coords = string_to_list(row.s_points_center)
    if validate_number_x(s_center_coords[0]) and validate_number_y(s_center_coords[1]):
        x_assis_s.append(s_center_coords[0])
        y_assis_s.append(s_center_coords[1])

for row in winner_df_r.itertuples():
    r_center_coords = string_to_list(row.r_points_center)
    if validate_number_x(r_center_coords[0]) and validate_number_y(r_center_coords[1]):
        x_assis_r.append(r_center_coords[0])
        y_assis_r.append(r_center_coords[1])

for row in winner_df_p.itertuples():
    p_center_coords = string_to_list(row.p_points_center)
    if validate_number_x(p_center_coords[0]) and validate_number_y(p_center_coords[1]):
        x_assis_p.append(p_center_coords[0])
        y_assis_p.append(p_center_coords[1])


# plot
fig, ax = plt.subplots()

ax.scatter(x_assis_s, y_assis_s, c="red")
ax.scatter(x_assis_r, y_assis_r, c="blue")
ax.scatter(x_assis_p, y_assis_p, c="green")

ax.set()

plt.show()
