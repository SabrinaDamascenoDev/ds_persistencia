import pandas as pd

df = pd.read_csv("../username.csv")

print(df)

df.to_csv("file_save.csv", index=False)

df.to_csv("file_save2.csv", index=False, sep=";")