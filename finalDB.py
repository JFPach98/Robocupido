import pandas as pd
import numpy as np

#Read and adapt data of survey
dfAll = pd.read_csv("data/enamoratec.csv")
dfAll = dfAll.iloc[:,[1,2,14,42,41]]
dfAll.columns = ['email', 'nombre', 'descripcion', 'tel', 'insta']

#Read and adapt results data
dfCasual = pd.read_csv("results/casual-valentines", header=None)
dfCasual[[0,1,3,5]] = dfCasual[[0,1,3,5]].astype('Int64')
dfRelation = pd.read_csv("results/relationship-valentines", header=None)
dfRelation[[0,1,3,5]] = dfRelation[[0,1,3,5]].astype('Int64')
dfFriend = pd.read_csv("results/friend-valentines", header=None, delimiter=',', names=list(range(20))).dropna(axis='columns', how='all')
dfFriend = dfFriend.astype('Int64')

#Count frequencies of candidates
c = dfCasual.stack().value_counts()
pd.DataFrame(c)
r = dfRelation.stack().value_counts()
pd.DataFrame(r)

#Build final df for Friends
dfFinalFriends = pd.DataFrame(columns=['First Name', 'Email', 'Valentine 1', 'insta1', 'tel1', 'Description 1', 'Valentine 2',  'insta2', 'tel2', 'Description 2', 'Valentine 3',  'insta3', 'tel3', 'Description 3','Valentine 4', 'insta4', 'tel4', 'Description 4'])
for row in range(dfFriend.shape[0]):
    i = 1
    for col in range(len(dfFriend.loc[row].dropna())):
        if col == 0:
            dfFinalFriends.at[row, 'First Name'] = dfAll.iloc[dfFriend.iloc[row,col],1]
            #dfFinalFriends.iloc[row,0] = dfAll.iloc[dfFriend.iloc[row,col],1]
            dfFinalFriends.at[row, 'Email'] = dfAll.iloc[dfFriend.iloc[row,col],0]
        else:
            #for i in range(1,5):
            dfFinalFriends.at[row, 'Valentine ' + str(i)] = dfAll.iloc[dfFriend.iloc[row,col],1]
            dfFinalFriends.at[row, 'insta' + str(i)] = dfAll.iloc[dfFriend.iloc[row,col],4]
            dfFinalFriends.at[row, 'tel' + str(i)] = dfAll.iloc[dfFriend.iloc[row,col],3]
            dfFinalFriends.at[row, 'Description ' + str(i)] = dfAll.iloc[dfFriend.iloc[row,col],2]
            i = i+1
#Export as CSV file
dfFinalFriends.to_csv(r'mail_data\finalDFfriends.csv', index = False)


#Build final df for Relationship
dfFinalRelation = pd.DataFrame(columns=['First Name', 'Email', 'Valentine 1', 'Porcentaje 1', 'insta1', 'tel1', 'Description 1', 'Valentine 2', 'Porcentaje 2', 'insta2', 'tel2', 'Description 2', 'Valentine 3', 'Porcentaje 3', 'insta3', 'tel3', 'Description 3', 'My Valentines'])
for row in range(dfRelation.shape[0]):
    i = 1
    for col in [0,1,3,5]:
        if col == 0:
            dfFinalRelation.at[row, 'First Name'] = dfAll.iloc[dfRelation.iloc[row,col],1]
            dfFinalRelation.at[row, 'Email'] = dfAll.iloc[dfRelation.iloc[row,col],0]            
        else:
            if pd.isnull(dfRelation.iloc[row,col]) == True:
                continue
            else:
                dfFinalRelation.at[row, 'Valentine ' + str(i)] = dfAll.iloc[dfRelation.iloc[row,col],1]
                dfFinalRelation.at[row, 'Porcentaje ' + str(i)] = dfRelation.iloc[row,col+1]
                dfFinalRelation.at[row, 'insta' + str(i)] = dfAll.iloc[dfRelation.iloc[row,col],4]
                dfFinalRelation.at[row, 'tel' + str(i)] = dfAll.iloc[dfRelation.iloc[row,col],3]
                dfFinalRelation.at[row, 'Description ' + str(i)] = dfAll.iloc[dfRelation.iloc[row,col],2]
                i = i+1
    dfFinalRelation.at[row, 'My Valentines'] = r.loc[dfRelation.loc[row,0]] - 1 
#Export as CSV file
dfFinalRelation.to_csv(r'mail_data\finalDFRelation.csv', index = False)

#Build final df for Casual
dfFinalCasual = pd.DataFrame(columns=['First Name', 'Email', 'Valentine 1', 'Porcentaje 1', 'insta1', 'tel1', 'Description 1', 'Valentine 2', 'Porcentaje 2', 'insta2', 'tel2', 'Description 2', 'Valentine 3', 'Porcentaje 3', 'insta3', 'tel3', 'Description 3', 'My Valentines'])
for row in range(dfCasual.shape[0]):
    i = 1
    for col in [0,1,3,5]:
        if col == 0:
            dfFinalCasual.at[row, 'First Name'] = dfAll.iloc[dfCasual.iloc[row,col],1]
            #dfFinalFriends.iloc[row,0] = dfAll.iloc[dfFriend.iloc[row,col],1]
            dfFinalCasual.at[row, 'Email'] = dfAll.iloc[dfCasual.iloc[row,col],0]
        else:
            if pd.isnull(dfCasual.iloc[row,col]) == True:
                continue
            else:
                dfFinalCasual.at[row, 'Valentine ' + str(i)] = dfAll.iloc[dfCasual.iloc[row,col],1]
                dfFinalCasual.at[row, 'Porcentaje ' + str(i)] = dfCasual.iloc[row,col+1]
                dfFinalCasual.at[row, 'insta' + str(i)] = dfAll.iloc[dfCasual.iloc[row,col],4]
                dfFinalCasual.at[row, 'tel' + str(i)] = dfAll.iloc[dfCasual.iloc[row,col],3]
                dfFinalCasual.at[row, 'Description ' + str(i)] = dfAll.iloc[dfCasual.iloc[row,col],2]
                dfFinalCasual.at[row, 'My Valentines'] = 3
                i = i+1
    dfFinalCasual.at[row, 'My Valentines'] = c.loc[dfCasual.loc[row,0]] - 1 
#Export as CSV file
dfFinalCasual.to_csv(r'mail_data\finalDFCasual.csv', index = False)
