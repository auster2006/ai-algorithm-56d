import pandas as pd

df = pd.read_csv("pandas/titanic.csv")

'''
print(df.head())

print("shape:")
print(df.shape)

print("columns:")
print(df.columns)

print("info:")
df.info()

print(df.isna().sum())
'''

df_clean = df.copy()

median_age = df_clean["Age"].median()
df_clean["Age"] = df_clean["Age"].fillna(median_age)

df_clean = df_clean.dropna(subset=["Embarked"])

print(df_clean.isna().sum())
print(df_clean.shape)



high_fare = df_clean[df_clean["Fare"] > 100]
print(high_fare[["Name", "Fare", "Pclass"]])

girls = df_clean[(df_clean["Age"] < 18)
         &
         (df_clean["Sex"] == "female")]
print(girls.shape[0])

print(df_clean.groupby("Sex")["Fare"].mean())

print(df_clean.groupby("Pclass")["Age"].mean())

print(df_clean.groupby("Pclass")["Survived"].mean())

result = df_clean.groupby("Sex").agg({
    "Age": "mean",
    "Fare": ["mean","median"],
    "Survived": "mean"
})

print(result)

print(df_clean.sort_values("Fare",ascending = False).head(10)[["Name", "Sex", "Pclass", "Fare"]])

print(df_clean.sort_values("Age").head(10)[["Name","Sex", "Age"]])

print(df_clean.describe())

print(df_clean[["Age", "Fare"]].describe())