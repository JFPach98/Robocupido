#!/usr/bin/env python
# coding: utf-8

# # Prepocessing and data cleansing

# This Jupyter Notebook is used, as its name indicates, to preproccess and to clean the data for the model of the project "Robocupido".

import pandas as pd
import numpy as np

df = pd.read_excel ('EnamóraTec_chido.xlsx')

cols = df.columns

df1 = df[cols[5:41]]

cols = df1.columns

def binarize(dataframe, column_name):
    series = list(dataframe[column_name])
    new_columns = []
    
    # column = list()
    for i in series:
        x = list(i.split(', '))
        for y in x:
            if y not in new_columns:
                new_columns.append(y)
    
    new_dataframe = pd.DataFrame(columns = new_columns)
    new_row = []
    for i in series:
        x = list(i.split(', '))
        for z in new_columns:
            if z in x:
                new_row.append(True)
            else:
                new_row.append(False)
        
        new_dataframe.loc[len(new_dataframe)] = new_row
        new_row = []
    
    column_names = list(dataframe.columns)
    index = column_names.index(column_name)
    dataframe = dataframe.drop(column_name, axis = 1)
    
    column_names_newdf = list(new_dataframe.columns)
    
    for x in column_names_newdf:
        dataframe.insert(loc=index, column=x, value=new_dataframe[x])
        index += 1
    
    return dataframe

new_df = binarize(df1, cols[11])

binarized_df = binarize(new_df, cols[-21])

contact = df[cols[41:45]]

binarized_df_final = pd.concat([binarized_df, contact], axis=1)

from pandas import ExcelWriter
writer = ExcelWriter('binarized_final.xlsx')
binarized_df_final.to_excel(writer,'Sheet1')
writer.save()

