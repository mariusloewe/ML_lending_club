
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def filter_by_std(series_, n_stdev=3.0, return_thresholds=False):
    mean_, stdev_ = series_.mean(), series_.std()
    cutoff = stdev_ * n_stdev
    lower_bound, upper_bound = mean_ - cutoff, mean_ + cutoff
    if return_thresholds:
        return lower_bound, upper_bound
    else:
        return [True if i < lower_bound or i > upper_bound else False for i in series_]
    
def filter_by_iqr(series_, k=1.5, return_thresholds=False):
    q25, q75 = np.percentile(series_, 25), np.percentile(series_, 75)
    iqr = q75-q25
    
    cutoff = iqr*k
    lower_bound, upper_bound = q25-cutoff, q75+cutoff
    
    if return_thresholds:
        return lower_bound, upper_bound
    else:
        return [True if i < lower_bound or i > upper_bound else False for i in series_]

def univariate_outlier_id_plot(df):
    color = "gray"
    fig = plt.figure(figsize=(12, 35))
    i=1
    for feature in df:        
        if feature == "Income":
          ser = df[feature].copy()
          ser.dropna(inplace=True)
        else:
          ser = df[feature]
        ax = fig.add_subplot(df.shape[1], 2, i)
        box = ax.boxplot(ser, flierprops=dict(markerfacecolor='r', marker='s'), vert=False, patch_artist=True)
        box['boxes'][0].set_facecolor(color)
        ax.set_title("Boxplot of "+feature)
        ax = fig.add_subplot(df.shape[1], 2, i+1)
        ax.hist(ser, density=1, bins=30, color=color, alpha=0.7, rwidth=0.85)
        ax.set_title("Histogram of "+feature)
        i+=2

    plt.tight_layout()
    plt.show()