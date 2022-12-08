from datetime import datetime

import time
timeone = datetime.now()
print("waiting")
time.sleep(5.5)
timetwo = datetime.now()

diff = timetwo - timeone
# Get the interval in milliseconds
diff_in_milli_secs = diff.total_seconds() * 1000
print('Difference between two datetimes in milli seconds:')
print(diff_in_milli_secs)

# df = pd.DataFrame()

# df2 = pd.DataFrame({
#     'a':[11,12,13],
#     'b':[15,16,17]
# })

#  df = df.append(df2, ignore_index = True )

#  df = df.append(df2, ignore_index = True )
# print(df)
# gfg_csv_data = df.to_csv("GfG.csv", index=True)


