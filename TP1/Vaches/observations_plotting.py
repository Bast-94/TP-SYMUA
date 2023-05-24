import matplotlib.pyplot as plt
import pandas as pd
import glob
import os
fichiers_csv = glob.glob('observation_curves/*.csv')

# Parcourir chaque fichier CSV
for fichier in fichiers_csv:
    df = pd.read_csv(fichier)
    fig, ax = plt.subplots()
    plt.plot(df.drop('Unnamed: 0',axis=1))
    plt.title(f'{fichier}')
    plt.xlabel('thicks')
    plt.ylabel('population')
    nom_sans_extension = os.path.splitext(fichier)[0]
    # Sauvegarder le graphique en tant qu'image
    plt.show()
    plt.savefig(f'{nom_sans_extension}.png')
    
    


    