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

new_subgroups = []

# Divides group into list of subgroups
def create_subgroup_list():
    global new_subgroups
    index = 0
    while index < len(new_subgroups):
        if (len(new_subgroups[index])>5):
            new_subgroups.append(new_subgroups[index][:int(len(new_subgroups[index])/2)])
            new_subgroups.append(new_subgroups[index][int(len(new_subgroups[index])/2):])
            new_subgroups.pop(index)
            index-=1
        index+=1

def main():
    print(dataframe.groupby('buscando').size())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # group people based on what they are looking for
    people_groups = []
    people_groups.append(dataframe.loc[dataframe['buscando'] == 'Amistad'])   # friends
    people_groups.append(dataframe.loc[dataframe['buscando'] == 'Pareja'])        # realtionship
    people_groups.append(dataframe.loc[dataframe['buscando'] == 'Algo Casual'])         # casual

    for group_index, group in enumerate(people_groups):
        print(group.shape)

        X_raw = np.array(group[["pelicula","Reggaeton","Electrónica","Pop","Instrumental","Rock","Metal","Cumbia","Kpop","Banda","anime","videojuegos","bailar","Futbol","Basquetbol","Baseball","Futbol Americano","Natación","Tennis","Ciclismo","No","Golf","taco","bbt","animal","helado","celebracion","estacion","pizza","astrologia","cocinar","cocinen","perrogato","pelilibros","subdub","temperatura","tiburon","poderes"]])
        y = np.array(group['id'])
        print(X_raw.shape)

        enc = preprocessing.OrdinalEncoder(categories='auto')
        enc.fit(X_raw)
        X = enc.transform(X_raw)

        number_of_clusters = 0

        # get K value
        if(group_index == 0):
            number_of_clusters = 40
        else:
            Nc = range(1, 30)
            kmeans = [KMeans(n_clusters=i) for i in Nc]
            score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
            kl = KneeLocator(range(1, 30), score, curve="concave", direction="increasing")
            number_of_clusters = kl.elbow
            print("Number of clusters: ", number_of_clusters)

        kmeans = KMeans(n_clusters=number_of_clusters).fit(X)
        centroids = kmeans.cluster_centers_
        # print(centroids)

        # Predicting the clusters
        labels = kmeans.predict(X)
        # Getting the cluster centers
        C = kmeans.cluster_centers_

        copy =  pd.DataFrame()
        copy['id']=group['id'].values
        copy['label'] = labels

        subgroups = []
        for i in range(0, number_of_clusters):
            subgroups.append(copy.loc[copy['label'] == i]['id'].tolist())
        print(len(subgroups))

        ## Uncomment for cluster stats
        # cantidadGrupo =  pd.DataFrame()
        # cantidadGrupo['cantidad']=copy.groupby('label').size()
        # print(cantidadGrupo)

        pairings = []
        # make people groups
        if(group_index == 0): # friends
            friend_groups = []
            for subgroup in subgroups:
                if(len(subgroup)>5):
                    global new_subgroups
                    new_subgroups.clear()
                    new_subgroups.append(subgroup.copy())
                    create_subgroup_list()
                    friend_groups = friend_groups + new_subgroups
                else:
                    friend_groups.append(subgroup)
            pairings = friend_groups.copy()
            print()
        # make partner groups
        else:
            id = group['id'].values.tolist()

            intereses = group['interes'].values.tolist()
            for index, interes in enumerate(intereses): intereses[index] = interes.split(', ')
            intereses_key = {"Mujeres":0, "Hombres":1, "No binarixs":2, "Género fluido":3, "Estoy aquí en busca de amigxs":4}
            for index, interes in enumerate(intereses):
                for index2, interest in enumerate(interes):
                    intereses[index][index2] = intereses_key[interest]

            genero = group['genero'].values.tolist()
            gender_key = {"Femenino":0, "Masculino":1, "No binarix":2, "Género fluido":3, "Prefiero no decirlo":3}
            for index, gender in enumerate(genero): genero[index] = gender_key[gender]

            mayor = group['mayor'].values.tolist()
            menor = group['menor'].values.tolist()
            edad = group['edad'].values.tolist()

            print("****************************************************")
            print("****************************************************")

            pairings = []
            left = []
            for subgroup in subgroups:
                posible_candidates = []
                # print(subgroup)
                for index, person in enumerate(subgroup):
                    posible_candidates.clear()
                    for candidate in (subgroup[:index] + subgroup[index + 1:]):
                        i_person = id.index(person)
                        i_candidate = id.index(candidate)
                        if(genero[i_candidate] in intereses[i_person]  and genero[i_person] in intereses[i_candidate]):
                            if not(((mayor[i_person] == "No" and edad[i_candidate]> edad[i_person]) or (menor[i_person] == "No" and edad[i_candidate] < edad[i_person])) or ((mayor[i_candidate] == "No" and edad[i_person]> edad[i_candidate]) or (menor[i_candidate] == "No" and edad[i_person] < edad[i_candidate]))):
                                ## Get likeness between candidate and person
                                candidate_likes = X[i_candidate].tolist()
                                person_likes = X[i_person].tolist()
                                counter_likes = 0
                                for index in range(0, len(candidate_likes)):
                                    if candidate_likes[index] == person_likes[index]:
                                        counter_likes+=1
                                likeness = counter_likes/len(candidate_likes)
                                posible_candidates.append([candidate, likeness])

                    ## Choose the three candidates that have the most likeness
                    max_index = [0, 0, 0]
                    max_likeness_candidates = []
                    for i in range (0, min(3,len(posible_candidates))):
                        max_likeness = posible_candidates[0][1]
                        for index, candidate in enumerate(posible_candidates):
                            if candidate[1] > max_likeness:
                                max_likeness = candidate[1]
                                max_index[i] = index
                        max_likeness_candidates.append(posible_candidates[max_index[i]])
                        posible_candidates.pop(max_index[i])
                    if(len(max_likeness_candidates)>0):
                        pairings.append([person, max_likeness_candidates])
                    else:
                        left.append(person)
            if len(left):
                for person in left:
                    posible_candidates = []
                    i_person = id.index(person)
                    for subgroup in subgroups:
                        for candidate in subgroup:
                            i_candidate = id.index(candidate)
                            if(genero[i_candidate] in intereses[i_person]  and genero[i_person] in intereses[i_candidate]) and person != candidate:
                                if not(((mayor[i_person] == "No" and edad[i_candidate]> edad[i_person]) or (menor[i_person] == "No" and edad[i_candidate] < edad[i_person])) or ((mayor[i_candidate] == "No" and edad[i_person]> edad[i_candidate]) or (menor[i_candidate] == "No" and edad[i_person] < edad[i_candidate]))):
                                    ## Get likeness between candidate and person
                                    candidate_likes = X[i_candidate].tolist()
                                    person_likes = X[i_person].tolist()
                                    counter_likes = 0
                                    for index in range(0, len(candidate_likes)):
                                        if candidate_likes[index] == person_likes[index]:
                                            counter_likes+=1
                                    likeness = counter_likes/len(candidate_likes)
                                    posible_candidates.append([candidate, likeness])
                    ## Choose the three candidates that have the most likeness
                    max_index = [0, 0, 0]
                    max_likeness_candidates = []
                    for i in range (0, min(3,len(posible_candidates))):
                        max_likeness = posible_candidates[0][1]
                        for index, candidate in enumerate(posible_candidates):
                            if candidate[1] > max_likeness:
                                max_likeness = candidate[1]
                                max_index[i] = index
                        max_likeness_candidates.append(posible_candidates[max_index[i]])
                        posible_candidates.pop(max_index[i])
                    pairings.append([person, max_likeness_candidates])            
            print(len(pairings))

        results_file_name = ''
        if group_index == 0:
            results_file_name = "results/friend-valentines"
        elif group_index == 1:
            results_file_name = "results/relationship-valentines"
        elif group_index == 2:
            results_file_name = "results/casual-valentines"

        ## write results
        with open(results_file_name, 'w') as f:
            write = csv.writer(f)
            write.writerows(pairings)
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    main()