import pandas as pd

data = {
    "Nome": ["Adilson", "Zumba", "Manuel"],
    "idade": [25, 30, 35],
    "Cidade": ["Luanda", "Tokyo", "New York"],
}

df = pd.DataFrame(data)
##print(df)
##print(df["idade"])
df["Profissão"] = ["Engenharia", "Analise", "Desenvolvimento"]
##print(df)

filtro = df[df["idade"] > 25]
print(df)
