import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

'''The following function creates a customized barplot'''

def barp(x,y,title):
    plt.title(title)
    sns.barplot(x=x,y=y)
