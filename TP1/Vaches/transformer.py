import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('Observations.csv')
df = df.drop("numéro du fichier csv d'observation", axis = 1)
# Convertir le dataframe en markdown
markdown_table = df.to_markdown(index=False)

# Afficher le résultat
print(markdown_table)