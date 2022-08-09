import pandas as pd

df = pd.read_csv(
    'base.csv',
    )

df.dropna(inplace=True)

new = df["categoria_4"].str.split(". ", n=1, expand=True)

df["Order"] = new[0]
df["Categoria"] = new[1]

order = df["Order"].astype(str).astype(int)
categoria = df["Categoria"]

df.drop(columns=["categoria_4"], inplace=True)

print(df)

print("********")

categories = pd.Categorical(
    df["Categoria"],
    ['Entre 3000 e 4000', 'Acima de 5000', '< 1200', 'Entre 1200 e 1500', 'Entre 1500 e 2000', 'Entre 2000 e 3000', 'Entre 4000 e 5000'],
    ordered=True
)

print(categories)

df["Categoria"] = df["Categoria"].cat.codes

print(df.head())
