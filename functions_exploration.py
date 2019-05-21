
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def correlation_matrix(data):
    correlation_matrix = data.corr()

    mask = np.zeros_like(correlation_matrix, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sb.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    return sb.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

def missing_values_reporter(df):    
    na_count = df.isna().sum() 
    ser = na_count[na_count > 0]
    return pd.DataFrame({"N missings": ser, "p missings": ser.divide(df.shape[0])})

#create violin and boxplots
def violin_box_plots(data):
    target = "Response"
    columns = data.columns

    for i in range(len(columns)):    
        fig, ax = plt.subplots(2, 1, sharex=True)
        sb.boxplot(data = data, y = columns[i], x = target, ax=ax[0])
        sb.violinplot(data = data, y = columns[i], x = target, split = True, ax=ax[1])
        plt.show()
        
def percentages_table(data):
    percentages = [.2, .4, .6, .8]
    num_data_Descr = round(data.describe(percentiles = percentages))
    return num_data_Descr

def describe_categoricals(data):
    cat_data_Descr = round(data.describe(include ='O'))
    return cat_data_Descr
    
def describe_cat(df, list_cfeatures, target):
    cat_list = []
    for feature in df[list_cfeatures]:    
        cat_list.append(data.groupby([feature]).agg({target: ['count', "mean"]}))
    return pd.concat(cat_list, axis=0, keys=list_cfeatures)

def low_variance_columns(data,std):
    percentages = [.2, .4, .6, .8]
    num_data_Descr = round(data.describe(percentiles = percentages))
    const=num_data_Descr.columns[num_data_Descr.loc["std"]<std]
    return print("Columns with zero or almost zero variance to be removed:\n", 
      list(const))