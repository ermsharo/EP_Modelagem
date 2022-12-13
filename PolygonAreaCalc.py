from shapely.geometry import Polygon
import pandas as pd
import ast

df = pd.DataFrame()
df = pd.read_csv("rand_simul.csv")


# print(df["init_of_r_pos"][0])


def string_to_list(str_of_list):
    res = ast.literal_eval(str_of_list)
    return res


def get_points_area(points):
    return Polygon(points).area


def get_points_density(area, number):
    return area / number


def get_points_center(points):
    center = Polygon(points).centroid
    return (center.x, center.y)


def add_collumns_df():
    s_points_area = []
    r_points_area = []
    p_points_area = []
    winner_points_area = []
    s_points_center = []
    r_points_center = []
    p_points_center = []
    winner_points_center = []
    s_points_density = []
    r_points_density = []
    p_points_density = []
    winner_points_density = []

    for row in df.itertuples():
        s_points = string_to_list(row.init_of_s_pos)
        r_points = string_to_list(row.init_of_r_pos)
        p_points = string_to_list(row.init_of_p_pos)
        w_points = string_to_list(row.winner_pos)

        s_area = get_points_area(s_points)
        r_area = get_points_area(r_points)
        p_area = get_points_area(p_points)
        win_area = get_points_area(w_points)

        s_points_area.append(s_area)
        r_points_area.append(r_area)
        p_points_area.append(p_area)
        winner_points_area.append(win_area)

        s_points_center.append(get_points_center(s_points))
        r_points_center.append(get_points_center(r_points))
        p_points_center.append(get_points_center(p_points))
        winner_points_center.append(get_points_center(w_points))

        s_points_density.append(get_points_density(s_area, row.count_of_s))
        r_points_density.append(get_points_density(r_area, row.count_of_r))
        p_points_density.append(get_points_density(p_area, row.count_of_p))
        winner_points_density.append(
            get_points_density(
                win_area, row.count_of_s + row.count_of_p + row.count_of_r
            )
        )

    df["s_points_area"] = s_points_area
    df["r_points_area"] = r_points_area
    df["p_points_area"] = p_points_area
    df["winner_points_area"] = winner_points_area

    df["s_points_center"] = s_points_center
    df["r_points_center"] = r_points_center
    df["p_points_center"] = p_points_center
    df["winner_points_center"] = winner_points_center

    df["s_points_density"] = s_points_density
    df["r_points_density"] = r_points_density
    df["p_points_density"] = p_points_density
    df["winner_points_density"] = winner_points_density

    # print("df", df)
    df2 = df
    df2.to_csv("rand_simul_new.csv", index=False)


add_collumns_df()


## Calcular a area entre os pontos
# print(" S - area", get_points_area(df["init_of_s_pos"][0]))
# print(" R - area", get_points_area(df["init_of_r_pos"][0]))
# print(" P - area", get_points_area(df["init_of_p_pos"][0]))
# print("centroid", get_points_center(df["init_of_p_pos"][0]))
# print("densidade", get_points_density(df["init_of_p_pos"][0]))

## Calcular a dispersão dos pontos


## Calcular o ponto central dos pontos de cada elemento


## Calcular o ponto central entre o ponto central dos elementos
