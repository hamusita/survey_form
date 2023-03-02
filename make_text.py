import pandas as pd

df = pd.read_csv("origin/text.csv", header=0)
df = df.sample(n=100)
df = df.reset_index(drop=True)

df.to_csv("sen.csv", header=False)