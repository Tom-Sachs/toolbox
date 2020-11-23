
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot


def numerical_features(df):
    '''Identifies numerical features in a dataset and stores them in a list.

    Parameters
    ----------

    df: DataFrame '''

    numerical_features = []

    for column in df.columns:
        if df[column].dtype in ['int8','int16','int32','int64','float16','float32','float64']:
            numerical_features.append(column)

    return numerical_features


def plot_features(df,numerical_features):
'''Plots distribution, boxplot and gaussianity of the feature.

Parameters
----------

df: Pandas DataFrame
numerical_features: List of strings

'''

# Loop over numerical columns to plot distribution, boxplot and gaussianity
    for numerical_feature in numerical_features:

        fig, ax =plt.subplots(1,3,figsize=(20,8))
        ax[0].set_title(f"Distribution of: {numerical_feature}")
        sns.histplot(data = df[numerical_feature], kde=True, ax=ax[0])
        ax[1].set_title(f"Boxplot of: {numerical_feature}")
        sns.boxplot(df[numerical_feature], ax=ax[1])
        ax[2].set_title(f"Gaussianity of: {numerical_feature}")
        qqplot(df[numerical_feature],line='s',ax=ax[2])
        fig.show()
