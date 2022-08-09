import pandas as pd

# reading csv to pandas
df = pd.read_csv(
    'base.csv',
    )

df.dropna(inplace=True)

# spliting each first number from each row
new = df["categoria_4"].str.split(". ", n=1, expand=True)

# adding to columns
df["Order"] = new[0]
df["Categoria"] = new[1]

# dropping table categoria_4
df.drop(columns=["categoria_4"], inplace=True)

# sorting categories in ascending
df2 = df.sort_values(["Order", "Categoria"])
print(df2)
