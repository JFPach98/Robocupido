import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn import preprocessing
import string
from kneed import KneeLocator
import csv

dataframe = pd.read_csv(r"data/binarized.csv")
dataframe_interest = dataframe.loc[dataframe['buscando'] != 'Amistad']
print(dataframe.shape)

gender_key = {"Femenino":0, "Masculino":1, "No binarix":2, "Género fluido":3, "Prefiero no decirlo":3}
gender_list = dataframe_interest['genero'].values.tolist()
for index, gender in enumerate(gender_list): gender_list[index] = gender_key[gender]

intereses = dataframe_interest['interes'].values.tolist()
for index, interes in enumerate(intereses): intereses[index] = interes.split(', ')
intereses_key = {"Mujeres":0, "Hombres":1, "No binarixs":2, "Género fluido":3, "Estoy aquí en busca de amigxs":4}
for index, interes in enumerate(intereses):
    for index2, interest in enumerate(interes):
        intereses[index][index2] = intereses_key[interest]

same_gender = 0
different_gender = 0
more_than_two_genders = 0

for index, gender in enumerate(gender_list):
    if len(intereses[index]) == 1:
        if gender in intereses[index]:
            same_gender+=1
        else:
            different_gender+=1
    else:
        more_than_two_genders+=1

print("Same gender", same_gender)
print("Different gender", different_gender)
print("More than 2 genders:", more_than_two_genders)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Genero")

print(dataframe.groupby('genero').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Buscando")

print(dataframe.groupby('buscando').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Amistad")

print(dataframe.loc[dataframe['buscando'] == 'Amistad'].groupby('genero').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Pareja")

print(dataframe.loc[dataframe['buscando'] == 'Pareja'].groupby('genero').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Algo casual")

print(dataframe.loc[dataframe['buscando'] == 'Algo Casual'].groupby('genero').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Taco")

print(dataframe.groupby('taco').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Helado")

print(dataframe.groupby('helado').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("pelicula")

print(dataframe.groupby('pelicula').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("animal")

print(dataframe.groupby('animal').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("celebracion")

print(dataframe.groupby('celebracion').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("astrologia")

print(dataframe.groupby('astrologia').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("signo")

print(dataframe.groupby('signo').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("temperatura")

print(dataframe.groupby('temperatura').size())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("poderes")

print(dataframe.groupby('poderes').size())