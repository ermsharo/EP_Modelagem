from shapely.geometry import Polygon
import pandas as pd

df = pd.DataFrame()
df = pd.read_csv("https://raw.githubusercontent.com/ermsharo/EP_Modelagem/main/rand_simul.csv")


print(df['init_of_s_pos'])


print("get area")

coords  = ((-1, 0), (-1, 1), (0, 0.5), (1, 1), (1, 0), (-1, 0))
polygon = Polygon(coords)
print(polygon.area)